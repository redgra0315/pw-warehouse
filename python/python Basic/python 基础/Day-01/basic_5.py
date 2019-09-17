#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'mi'
__mtime__ = '2019/9/17'      
"""
for i in range(10):
    if i < 4:
        if i == 1:
            print(i, "st")
        elif i == 2:
            print(i, "nd")
        else:
            print(i, "rd")
    else:
        print(i, "th")
