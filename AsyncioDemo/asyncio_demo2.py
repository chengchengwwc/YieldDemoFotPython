#!/usr/bin/env python
# -*- coding:utf-8 -*-

import asyncio
import time
from functools import partial

async def get_html(url):
    print ("start html")
    await asyncio.sleep(2)
    print ("end html")
    return "body"

def callback(url,future):
    print (url)
    print ("send email")


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    #get_future = asyncio.ensure_future(get_html("DDDD"))
    task = loop.create_task(get_html("DDD"))
    task.add_done_callback(partial(callback,"ddd"))
    tasks = [get_html("D") for i in range(10)]
    loop.run_until_complete(task)
    print (task.result())