'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-09-05 17:21:51
@LastEditTime: 2019-09-05 17:46:19
@LastEditors: Please set LastEditors
'''
#/usr/bin/env  python

#给定一个不超过5位的正整数，判断该数的位数，依次打印出个位、十位、百位、千位、万位的数字
#方法一：
    # a = int(input("Please enter a number: "))
    # length = 0
    # if a < 0:
    #     print('Error')
    # elif a < 1000:
    #     if 9 < a < 100:
    #         length = 2
    #     elif a < 10:
    #         length = 1
    #     else:
    #         length = 3
    # elif a < 10000:
    #     length = 4
    # elif a < 100000:
    #     length = 5
    # else:
    #     print('Error')
    # print("输入的参数为：",length, "位数")
    # print("依次打印出个位、十位、百位、千位、万位的数字")
    # for i in range(length):
    #     print(a % 10)
    #     a = a // 10

#方法二：
# a = input("Please  enter a number:")
# b  = int(a)
# print("参数的长度为：%d" %(len(a)))
# for i  in range(len(a)):
#     print(b % 10)
#     b = b // 10

#方法三：
a=int(input("Please enter a number: "))
a *= 10
while (a // 10) != 0:
    a //= 10
    print(a % 10)