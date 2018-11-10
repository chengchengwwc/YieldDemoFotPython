#!/usr/bin/env python
# -*- coding:utf-8 -*-

import aiohttp
import aiomysql
import asyncio
from pyquery import PyQuery
import re

start_url = 'http://www.jobbole.com/'
waitiing_urls = []
seen_urls = set()
stopping = False


async def fetch(url,session):
    try:
        async with session.get(url) as resp:
            print (resp.status)
            if resp.status in [200,201]:
                data = await resp.text()
                return data
    except Exception as e:
        print (e)
        return None


def extract_urls(html):
    urls = []
    pq = PyQuery(html)
    for link in pq.items("a"):
        url = link.attr("href")
        if url and url.startswith("http") and url not in seen_urls:
            urls.append(url)
            waitiing_urls.append(url)
    return urls



async def init_urls():
    html = await fetch(start_url)
    extract_urls(html)

async def article_handler(url,session,pool):
    html = await fetch(url,session)
    seen_urls.add(url)
    extract_urls(html)
    pq = PyQuery(html)
    title = pq("title").text()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.excute("insert")







async def consumer(pool):
    async with aiohttp.ClientSession() as session:
        while not stopping:
            if len(waitiing_urls) == 0:
                await asyncio.sleep(0.5)
                continue
            url = waitiing_urls.pop()
            print (url)
            if re.match('http://.*?jobbole.com/\d+/',url):
                if url not in seen_urls:
                    asyncio.ensure_future(article_handler(url,session,pool))


async def main(loop):
    #wait mysql connection
    pool = await aiomysql.create_pool(host='127.0.0.1',
                                      port=3306,
                                      db='mysql',
                                      loop=loop,
                                      password='',
                                      charset='utf8',
                                      autocommit=True)

    async with aiohttp.ClientSession() as session:
        html = await fetch(start_url,session)
        seen_urls.add(start_url)
        extract_urls(html)
    asyncio.ensure_future(consumer(pool))


if __name__ == "__main__":
    loog = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop=loog))
    loog.run_forever()

