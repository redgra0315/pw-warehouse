#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "mi"
__mtime__ = "2019/9/26"      
"""


def build_person(first_name, last_name, age):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person["age"] = age
    return person


musician = build_person('jami', 'hendrix', 45)
print(musician)
