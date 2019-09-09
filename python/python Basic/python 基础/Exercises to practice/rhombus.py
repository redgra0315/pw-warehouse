'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-09-06 10:10:02
@LastEditTime: 2019-09-06 10:15:56
@LastEditors: Please set LastEditors
'''
#打印菱形
#方法1

# a = int(input("enter a number:"))
# b = (a - 1) / 2
# for i in range(a):
#     if i <= b:
#         print(' ' * ((a - (2 * i + 1)) // 2) +'*' * (i * 2 + 1) + ' ' * (( a - (2 * i + 1)) // 2 ))
#     else:
#         m=int(2 * b - i)
#         print(' '*((a - (2 * m + 1)) // 2) +'*' * (m * 2 + 1) +' ' * ((a - (2 * m + 1)) // 2))

a = int(input("enter a number:"))
b = (a - 1) // 2
for i in range(-b,b +1 ):
    c = abs(i)
    print(" "  * c + '*'  * ( a - 2 * c) + '' * c)
