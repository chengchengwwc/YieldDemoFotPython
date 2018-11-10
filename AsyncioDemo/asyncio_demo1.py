#!/usr/bin/env python
# -*- coding:utf-8 -*-


#事件循环
#回调
#多路复用
#asyncio 是python 用于解决异步io编程的一整套解决方案
#tornado 可以直接部署

import asyncio
import time

async def get_html(url):
    print ("start html")
    await asyncio.sleep(2)
    print ("end html")


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html("D") for i in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.run_until_complete(asyncio.gather(*tasks))
    print (time.time()-start_time)

"""
gather and wait
gather can make group

"""
