
def conunter(bash):

    def inc(step=1):
        nonlocal bash
        bash = bash + step
        return bash

    return inc


foo = conunter(10)
print(foo)

foo1 = conunter(10)

print(foo1)
