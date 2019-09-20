#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "mi"
__mtime__ = "2019/9/19"      
"""
db = {}
lst = []

count = 0
five = 2
# country_scenic_info =  {}
# scenic_info = []

# while count < five:
#     value = input("请输入你要去的国家：")
#     count_1 = int(input("请输入你选择城市的个数："))
#     lst_1 = lst[:]
#     for i in range(count_1):
#         value_1 = input("请输入你选择的城市:")
#         lst_1.append(value_1)
#         # lst.clear()
#     db[value] = lst_1
#     count += 1
# print(db)
import sys

information = """
    A) 根据国家来查找景点
    B）根据景区选择国家
    Q）退出
"""

db = {'中国': ['香港', '台湾', '澳门'], '美国': ['华盛顿', '纽约', '洛杉矶']}
print("---If you could visit one placein the world, where would you go?---")
while True:
    print(information)
    value = input("To see which countries you can choose to travel to, press ok:").lower()
    print(value)
    if value.lower() not in "abq":
        print("Wrong selection, please try again!")
        break
    if value == "a":
        name = list(db.keys())
        country = int(input("Please select country (from 0 to 10): "))
        Selected_countries = name[country]
        name_value = db.get(Selected_countries)
        city_count = len(name_value)
        print("你所在地位:{0}，可以选择{1}个城市:".format(Selected_countries, city_count),
              "\t 城市分别是：%s" % name_value)
        City_Numbers = int(input("Tips: select by number (from 0 to 10): "))
        print("Congratulations, your choice is {0},{1}".format(Selected_countries, name_value[City_Numbers]))
    else:
        print("结束")
        sys.exit(0)
