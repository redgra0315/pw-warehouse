# -*-encoding:UTF-8 -*-

''' 
异步I/O操作 - async 和 await
'''


import  asyncio

import threading

async def hello():
    print("%s: hello world!" % threading.current_thread())
    await asyncio.sleep(2)
    print("%s: goodbye, world!" % threading.current_thread())
loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()