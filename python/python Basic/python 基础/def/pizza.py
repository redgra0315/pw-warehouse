#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "mi"
__mtime__ = "2019/10/14"      
"""


def make_pizza(size, *args):
    """概述要制作的比萨"""
    print("\n Making a " + str(size) +
          " -inch pizza with the following toppings:")
    for topping in args:
        print("- " + topping)
