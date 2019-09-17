#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'mi'
__mtime__ = '2019/9/17'      
"""
# age_value = int(input("Please enter your guess age:"))
# if age_value < 0:
#     print("ERROR")
# if age_value >= 20:
#     if 20 < age_value < 65:
#         print("成年人")
#     else:
#         print("老年人")
# else:
#     if 0 < age_value < 2:
#         print("婴儿")
#     elif 2 < age_value < 4:
#         print("正在学习走路")
#     elif 4 < age_value < 13:
#         print("儿童")
#     else:
#         print("青少年")

favorite_fruits = ['apple', 'kiwi fruit', 'pitaya']
for _ in range(5):
    fruits = input("Please enter fruit name:")
    if fruits in favorite_fruits:
        print("Your really like bananas!")
    else:
        print("Fruit does not exist")