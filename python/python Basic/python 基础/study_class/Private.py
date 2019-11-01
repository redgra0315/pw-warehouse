#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = "私有属性"
__author__ = "mi"
__mtime__ = "2019/10/29"      
"""


class Prrson:
    def __init__(self, chinese,name, age=18):
        # self._chinese = chinese
        self._name = name
        self.__age = age

    def getname(self):
        return self._age

    def getage(self):
        return self._name

    def setname(self,value):
        self._name = value
    @property
    def chinese(self):
        return self.__age

    @chinese.setter
    def chinese(self,value):
        self.__age  = value
    @chinese.deleter
    def chinese(self):
        print("hah")
stu = Prrson(21,"TOM",254)
print(stu.chinese)