#!/usr/bin/env python
# -*- coding:utf-8 -*-

import asyncio


async def get_url(url):
    print ("start")
    reader,writer = await asyncio.open_connection("127.0.0.1",80)
    writer.write("DDDDDSS")
    all_lines = []
    async for raw_line in reader:
        line = raw_line.decode("utf-8")
        all_lines.append(line)
    html = "\n".join(all_lines)
    return html

async def main():
    tasks = []
    for url in range(10):
        tasks.append(asyncio.ensure_future(get_url(url)))

    for task in asyncio.as_completed(tasks):
        result = await task
        print (result)



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())










