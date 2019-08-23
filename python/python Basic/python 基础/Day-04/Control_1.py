# -*- encoding: utf-8 -*-
'''
@File    :   Control_1.py
@Time    :   2019/08/21 16:26:59
@Version :   1.0
@Contact :   redgra0315@163.com
@Desc    :   None
'''

# here put the import lib

x = int(input("Please enter an integer:"))
if x < 0:
    print("Negative changed to zero")
elif x == 1:
    print('Zero')
elif x == 0:
    print("Single")
else: 
    print('More')
