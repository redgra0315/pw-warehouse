#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "mi"
__mtime__ = "2019/10/30"      
"""


class Car:
    def __init__(self, mark, speed, color, price):
        self.mark = mark
        self.speed = speed
        self.color = color
        self.price = price


class CatInfo:
    def __init__(self):
        self.lst = []

    def addcar(self, car: Car):
        self.lst.append(car)


    def getall(self):
        print("hehe")
        return self.lst


ci = CatInfo()
car = Car("AUDI", 500, "greed", 200)
ci.addcar(car)


b = ci.getall()

print(CatInfo.__dict__)
