#!/usr/bin/env python
# -*- coding:utf-8 -*-


import asyncio
from concurrent.futures import ThreadPoolExecutor
import time


def get_url(url):
    print ("strat url")
    print (url)
    time.sleep(2)
    print ("end")


if __name__ == "__main__":
    start_time = time.time()
    tasks = []
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor()
    for url in range(10):
        task = loop.run_in_executor(executor,get_url,url)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    end_time = time.time()
    print (end_time-start_time)

