#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 1 . run_until_complete
import asyncio
import time


async def get_html(sleep_time):
    print ("waiting")
    await asyncio.sleep(sleep_time)
    print ("done {}".format(sleep_time))


if __name__ == "_main__":
    task1 = get_html(2)
    task2 = get_html(3)
    task3 = get_html(3)
    loop = asyncio.get_event_loop()
    tasks = [task1,task2,task3]
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        all_tasks = asyncio.Task.all_tasks()
        for task in all_tasks:
            print ("cancel task")
            task.cancel()
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()


