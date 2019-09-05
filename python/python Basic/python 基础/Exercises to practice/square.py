'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-09-05 18:21:17
@LastEditTime: 2019-09-05 18:28:25
@LastEditors: Please set LastEditors
'''
#!/usr/bin/env python 

#打印一个边长为n的正方形
#方法一
# a = int(input("Please enter a number: "))
# for i in range(a):
#     if i == 0 or i == a-1:
#         print('*' * a )
#     else:
#         print('*' + ' ' * (a - 2) + '*')


#方法二
a = int(input("Please enter a number: "))
top = mid = '*'
for i in range(a - 1):
    top += '\t*'
    mid += '\t'
else:
    mid += '*'
    print(top)

for i in range(a - 2):
    print('\n')
    print(mid)
else:
    print('\n')
    print(top)