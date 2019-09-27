#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = "Tourists travel"
__author__ = "mi"
__mtime__ = "2019/9/19"      
"""

"""
先设置两个列表:
     一个里面存放国家
     一个里面存放旅游景点
     之后在把列表打印出来，使用索引的方式在添加到字典里面，最后把字典根据城市来进行展示
     
     
"""

import sys


def set_scenic(state_count=2):
    count = 0
    country_scenic_info = {}
    scenic_info = []
    while True:
        value = input("请输入你要去的国家：")
        state_count = int(input("请输入你选择城市的个数："))
        lst_1 = scenic_info[:]
        for _ in range(state_count):
            value_1 = input("请输入你选择的城市:")
            lst_1.append(value_1)
        country_scenic_info[value] = lst_1
        count += 1
        add_status = input("是否继续添加 (yes/no)? ")
        if add_status == "no":
            break
        count = 0
    return country_scenic_info


def Destination():
    db = set_scenic()
    print("---If you could visit one placein the world, where would you go?---")
    information = """
        A) 根据国家来查找景点
        S) 根据景点来查找国家
        Q）退出
    """
    while True:
        print(information)
        value = input("To see which countries you can choose to travel to, press ok:").lower()
        print(value)
        if value.lower() not in "abq":
            print("Wrong selection, please try again!")
            break
        if value == "a":
            name = list(db.keys())
            print(name)
            country = int(input("Please select country (from 0 to 10): "))
            Selected_countries = name[country]
            name_value = db.get(Selected_countries)
            city_count = len(name_value)
            print("你所在地位:{0}，可以选择{1}个城市:".format(Selected_countries, city_count),
                  "\t 城市分别是：%s" % name_value)
            City_Numbers = int(input("Tips: select by number (from 0 to 10): "))
            print("Congratulations, your choice is {0},{1}".format(Selected_countries, name_value[City_Numbers]))
        elif value == "s":
            name = list(db.values())
            lst_set = name[0] + name[1]
            print("以下景点可供你做选择:", lst_set)
            unist = input("请输入你要选择的景点:")
            for key, value in db.items():
                if unist in value:
                    print(f'城市:{unist} 国家:{key}')
        else:
            return "结束"
            sys.exit(0)


info = Destination()
print(info)
