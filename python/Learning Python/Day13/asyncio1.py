# -*-encoding:UTF-8 -*-

"异步I/O操作 - asyncio模块"
import asyncio
import threading
from time  import  time


@asyncio.coroutine
def hello():
    print("%s:hello,world!" % threading.current_thread())
    yield from asyncio.sleep(2)
    print("等待时间为%d" % time())
    print("%s: goodbye,world!" % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]

loop.run_until_complete(asyncio.wait(tasks))
print('game over!')
loop.close()



