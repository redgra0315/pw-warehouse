'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-08-27 17:08:42
@LastEditTime: 2019-08-27 17:38:57
@LastEditors: Please set LastEditors
'''
# -*- encoding: utf-8 -*-
'''
@File    :   for_4.py
@Time    :   2019/08/27 17:08:45
@Version :   1.0
@Contact :   redgra0315@163.com
@Desc    :   None
'''

for i in range(-70,69):
    if i<0:       #if..else..条件可以写成三木运算符形式
        j=-i      #  j=-i if i<0 else j=i
    else:
        j=i
    #先是j个空格，然后打印（9-2j）个* ，后面的都是空格，在屏幕上不显示，可以不打印#
    # print(" " *j + "*" * ( 131-2*j))   
    print(j,131-2*j)



import copy
copy.deepcopy