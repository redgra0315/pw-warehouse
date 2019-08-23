'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-08-22 16:31:26
@LastEditTime: 2019-08-22 16:52:05
@LastEditors: Please set LastEditors
'''
# -*- encoding: utf-8 -*-
'''
@File    :   for_2.py
@Time    :   2019/08/22 16:38:52
@Version :   1.0
@Contact :   redgra0315@163.com
@Desc    :   None
'''

# here put the import lib



# for n in range(2,10):
#     for i in range(2,n):
#         if n % i == 0:
#             print(n,'equals',i, '*', n//i)
#             break
#     else:
#         print(n,"is a prime number")
            
for num in range(2,10):
    if num % 2 ==0:
        print("Found an even number",num)
        continue
    print("Found a number",num)
    