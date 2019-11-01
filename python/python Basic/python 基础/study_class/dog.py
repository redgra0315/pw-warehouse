#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "mi"
__mtime__ = "2019/10/14"      
"""


# class Dog():
#     """一次模拟小狗的简单尝试"""
#
#     def __init__(self, name, age):
#         """初始化属性name和age"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """模拟小狗被命令时蹲下"""
#         return self.name.title() + "is now sitting. " + "age is:" + str(self.age)
#
#     def roll_over(self):
#         """模拟小狗被命令时打滚"""
#         return self.name.title() + " rolled over," + "age is:" + str(self.age)
#
#
# my_dog = Dog('willie',6)
# my_top = my_dog.sit()
# print(my_top)
# my_boy = my_dog.roll_over()
# print(my_boy)

class Person:
    @classmethod  #类方法

    def class_method(cls):
        print('class = {0.__name__} ({0})'.format(cls))
        cls.HEIGHT = 170

    @staticmethod
    def static_methd():
        print(Person.HEIGHT)

Person.class_method()
Person.static_methd()
print(Person.__dict__)
