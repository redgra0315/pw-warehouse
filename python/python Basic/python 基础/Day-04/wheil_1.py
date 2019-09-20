#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'mi'
__mtime__ = '2019/9/18'      
while:
    break      退出整个循环
    continue   跳过本次循环
"""


# prompt = "\nTell me something, and I will repeat it back to you,"
# prompt += "\nEnter 'quit' to end the program: "
# active = True
# while True:
#     message = input(prompt)
#     if message == 'quit':
#         break
#         # active = False
#         print("Wabash")
#     else:
#         print(message)
# print()

# correct_count = 0
# while correct_count < 10:
#     correct_count += 1
#     if correct_count % 2 == 0:
#         continue
#     print(correct_count)

while True:
    material = input("Please input the required materials：")
    if material == "quit":
        break
    print("The material is:", material)

