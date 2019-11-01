#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "mi"
__mtime__ = "2019/10/30"      
"""


# class Temper:
#     def __init__(self, c=None, f=None, k=None):
#         self.c = c
#         self.f = f
#         self.k = k
#
#
#     def getk(self):
#         return self.k
#
#     def getf(self):
#         return self.f
#
#     def getc(self):
#         return self.c
#
#     @classmethod
#     def c2f(cls, c):
#         return


class Item:
    def __init__(self):
        pass


class Color:
    pass
class Cart:
    def __init__(self):
        self.lst = []

    def additem(self, item:Item):
        self.lst.append(item)



