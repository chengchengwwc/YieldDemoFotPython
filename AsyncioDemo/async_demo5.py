#!/usr/bin/env python
# -*- coding:utf-8 -*-

import asyncio


def callback(sleep_times):
    print (sleep_times)

def stop_loop(loop):
    loop.stop()



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    #loop.call_soon(stop_loop, loop)
    loop.call_soon(callback,2)
    loop.call_later(5,callback,3)

    loop.run_forever()