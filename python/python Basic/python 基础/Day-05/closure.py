'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-09-10 14:08:23
@LastEditTime: 2019-09-10 14:08:23
@LastEditors: your name
'''
#闭包

def counter():
    c = [0]
    def inc():
        c[0] += 1
        return c[0]
    return inc

foo = counter()
print(type(foo))