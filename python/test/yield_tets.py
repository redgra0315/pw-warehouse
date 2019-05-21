# -*- encoding:UTF-8 -*-
''' def yield_test(n):
    for i in range(n):
        yield call(i)
        print('i= ', i)
    print("di something")
    print("end .")


def call(i):
    return i * 2


for i in yield_test(5):
    print(i, ',') '''
import asyncio

async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    #nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())
