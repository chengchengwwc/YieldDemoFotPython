#!/usr/bin/env python
# -*- coding:utf-8 -*-

import asyncio
from asyncio import Lock,Queue
import aiohttp

lock = Lock()
cache = {}
await queue.put()

async def get_stuff(url):
    async with lock:
        if url in cache:
            return cache[url]
        stuff = await aiohttp.request('GET',url)
        cache[url] = stuff
        lock.release()
        return stuff



async def parse_stuff():
    stuff = await get_stuff()
    pass

async def use_stuff():
    stuff = await get_stuff()
    pass

