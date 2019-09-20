#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'mi'
__mtime__ = '2019/9/17'      
获取字典中列表的值进行对比
人员调查表,如果不在名单中有个判断语句
"""
import sys

db_1 = {"sum_number": ["jack", "tom", "carl", "Bill", "Tina", "Fred"]}
while True:
    number_value1 = input("请输入名字：")
    if number_value1 in db_1["sum_number"]:
        print("他在邀请人员的名单中")
    else:
        print("抱歉，你不在名单中")
        continue_firam = input("是否要继续玩(y|n)!")
        if continue_firam != 'n':
            db_1["sum_number"].append(number_value1)
        else:
            print("尊重你的选择!")
            sys.exit(1)
    print("以下人员可以参加会议", db_1.values())
    # sys.exit(0)
