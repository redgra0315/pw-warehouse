#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'Pizza toppings'
__author__ = 'mi'
__mtime__ = '2019/9/17'      
"""
#第一个示例


name_list = ['tom', 'admin', 'reaches', 'hen', 'jack']
for _ in range(len(name_list)):
    name_value = input("Enter is name:")
    if name_list == "":
        print("We need to find some users")
    else:
        if name_value == name_list[1]:
            print("Hello " + name_value + "," + "would you like to see a status report?")
        else:
            print("Hello " + name_value + "," + "thank you for logging in again")
name_list.clear()
print(name_list)


