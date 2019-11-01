#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = "方法的重写、覆盖override"
__author__ = "mi"
__mtime__ = "2019/10/31"      
"""


class Animal:
    def shout(self):
        print("Animal shout")


class Cat(Animal):

    def shout(self):
        super().shout()
        print("miao")


A = Cat()
A.shout()

print(A.__dict__)
