#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'mi'
__mtime__ = '2019/9/18'      
"""
# 第一种
# count = 0
# while count < 5:
#     agv = int(input("Please input agv:"))
#     if agv < 0 :
#         print("The parameters are incorrect, please try again")
#         continue
#     if agv <= 3:
#         print("The audience for free!")
#     elif 3 < agv < 12:
#         print("Admission is $10!")
#     else:
#         print("Admission is $15!")
#     count += 1
# print("good bey")


# 第二种
while True:
    agv = int(input("Please input agv:"))
    if agv < 0:
        print("The parameters are incorrect, please try again")
        continue
    if agv <= 3:
        print("The audience for free!")
    elif 3 < agv < 12:
        print("Admission is $10!")
    else:
        print("Admission is $15!")
        value = input(""" Whether to continue playing,Press any key to continue and "quit:" """)
        if value == "quit":
            break
