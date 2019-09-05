'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-09-05 17:47:19
@LastEditTime: 2019-09-05 18:13:32
@LastEditors: Please set LastEditors
'''
#!/usr/bin/env python 
#.给定一个不超过5位的正整数，判断该数的位数，依次打印出万位、千位、百位、十位、个位的数字
# a=input('Please enter a number: ')
# b=int(a)
# for i in range(len(a),0,-1):
#     te = 10 ** (i - 1)
#     print(te)
#     c = b // te
#     print(c)
#     b -= (c * te)
# print("长度为:",len(a),"位数")   


#方法二：
c = int(input("Please enter a number: "))
w = 10000
length = 5
flag = False
while w:
    t = c // w
    if flag:  
        print(t)
    else:     
        if t:
            print(t)
            flag = True
        else:
            length -= 1
    c = c % w 
    w //= 10
print("The length of number is", length)