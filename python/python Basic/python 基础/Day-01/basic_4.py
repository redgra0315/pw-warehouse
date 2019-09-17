#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'mi'
__mtime__ = '2019/9/17'      
"""
# 创建一个包含5个用户名的列表 current_users
# 在创建一个包含5个用户名的列表 new_users,并确保一两个用户名包含在current_users中


current_users = ['tom', 'admin', 'Karen', 'Irene', 'Nick', 'Diego', 'Emma', 'Jack']
new_users = ['Emma', 'Larissa', 'jack', 'Joyce', 'Kelly']

for i in new_users:
    if i.lower() in " ".join(current_users).lower():
        print(i.title(), "Already in use")
    else:
        print(i, "Not used!")
