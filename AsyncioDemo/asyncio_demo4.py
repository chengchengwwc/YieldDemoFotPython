#!/usr/bin/env python
# -*- coding:utf-8 -*-

import asyncio


async def compute(x,y):
    print (x,y)
    await asyncio.sleep(1)
    return (x+y)

async def print_sum(x,y):
    result = await compute(x,y)
    print (result)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_sum(1,2))
    loop.close()
