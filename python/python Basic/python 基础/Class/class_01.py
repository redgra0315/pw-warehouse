#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "mi"
__mtime__ = "2019/9/27"      
"""


class Person:
    '这是一个学习Python定义的一个Person类'
    # 下面定义了一个类变量
    hair = 'black'

    def __init__(self, name, age=8):
        # 下面为Person对象增加2个实例变量
        self.name = name
        self.age = age

    # 下面定义了一个say方法
    def say(self, content):
        return content


a = Person('haha')
print(a.name, a.age)
print(a.say(1))

print(a.__class__.__qualname__,a.__dict__)


