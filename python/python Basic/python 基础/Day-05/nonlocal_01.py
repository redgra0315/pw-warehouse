'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-09-10 16:37:44
@LastEditTime: 2019-09-10 17:07:23
@LastEditors: Please set LastEditors
'''
def counter():
    count = 0 
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
foo = counter()
#print(foo())
print(foo.__defaults__)
