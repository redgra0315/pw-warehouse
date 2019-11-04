#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "mi"
__mtime__ = "2019/11/4"      
"""
import logging
from functools import wraps



# 第一个例子
# def use_logging(level):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if level == "warn":
#                 logging.warning("%s is running" % func.__name__)
#             elif level == "info":
#                 logging.info("%s is running" % func.__name__)
#             return func(*args)
#
#         return wrapper
#
#     return decorator
#
#
# @use_logging(level="warn")  # foo = use_logging(foo)
# def foo(name):
#     print("i am %s" % name)


# foo("admin")


# 第二个例子

def loggend(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__)
        print(func.__doc__)
        return func(*args, **kwargs)

    return with_logging


@loggend
def f(x):
    """does some math"""
    return  x  + x * x


print(f(3))
