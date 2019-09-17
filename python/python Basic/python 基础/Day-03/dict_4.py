#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'mi'
__mtime__ = '2019/9/17'      
"""
db = {}

for i in range(4):
    name = input("请输入用户名:")
    # 根据关键字 name 查看字典中是否已存在此键值对
    if name in db:
        # if db.has_key(name):
        print("该用户名已经存在，请重试")
        continue

    pwd = input("input your password:")
    # 存账号密码到字典中
    db[name] = pwd
    print("已经存在字典中")
print(db)
