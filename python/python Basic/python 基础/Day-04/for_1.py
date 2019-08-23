'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-08-21 16:39:56
@LastEditTime: 2019-08-22 16:24:34
@LastEditors: Please set LastEditors
'''
# -*- encoding: utf-8 -*-
'''
@File    :   for_1.py
@Time    :   2019/08/21 16:39:59
@Version :   1.0
@Contact :   redgra0315@163.com
@Desc    :   None
'''

# here put the import lib



words = ["Cat","Windows","Linux","Mac"]
# for w in words:
#     print(w,  '-->', len(w))


# for w in words[:]:
#     if len(w) > 6:
#         words.insert(0,w)
# print(words)


# 要迭代序列的索引，您可以组合range()并 len()如下：
words = ["Cat","Windows","Linux","Mac"]
# for i in range(len(words)):
#     print(i,words[i])


for i in enumerate(words):
    print(i)
    