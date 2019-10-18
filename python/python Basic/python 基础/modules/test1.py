#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "mi"
__mtime__ = "2019/10/17"      
"""
print("this is   test1 module")


class A:
    def show(self):
        print(type(self).__name__)


a = A()
a.show()
