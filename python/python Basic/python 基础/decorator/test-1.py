#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "mi"
__mtime__ = "2019/11/1"      
"""

from functools import wraps

# def log_func_name(func):
#     "打印函数名"
#     def wrapper(*args):
#         print("函数{}正在运行".format(func.__name__))
#         func(*args)
#     return wrapper
#
# @log_func_name
# def say_hello(cut):
#     for _ in range(cut):
#         print("hello")
#
# if __name__ == '__main__':
#     say_hello(3)
#
#
#
# 第一个装饰器
# def log_func_name(func):
#     '''打印函数名'''
#     def wrapper(*args, **kwargs):
#         print('函数{}正在运行'.format(func.__name__))
#         func(*args, **kwargs)
#     return wrapper
#
# @log_func_name
# def say_hell(cnt):
#     '''打印hello'''
#     for _ in range(cnt):
#         print('hello')
# say_hell = log_func_name(say_hello)
#
# if __name__ == '__main__':
#     say_hell(3)
#
# # 第二个装饰器
#
# def log(func):
#     def wrapper():
#         print("log  开始……")
#         func()
#         print("log  结束……")
#     return  wrapper
# @log
# def main():
#     print("test")
#
# if __name__ == '__main__':
#     main()

# 使用functools模块提供的修改函数属性的方法wraps


# from functools import  wraps
#
#
# def log(func):
#     @wraps(func)
#     def wrapper():
#         print("log 开始……")
#         func()
#         print("结束……")
#     return wrapper
#
# @log
# def test1():
#     print("test1....")
#
#
# def test2():
#     print("test2....")
#
# print(test1.__name__)
# print(test2.__name__)

# 例子3：被修饰函数带参数


# def log(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print("log 开始...", func.__name__)
#         ret = func(*args, **kwargs)
#         print("log 结束...")
#         return  ret
#     return wrapper
#
# @log
#
#
# def test1(s):
#     print("test1...",s)
#     return  s
#
#
# @log
#
# def test2(s1, s2):
#     print("test2 ...", s1, s2)
#     return s1 + s2
#
# test1("asd")
# test2("as", "fd")


# 例子4：修饰符带参数，需要比上面例子多一层包装


# def log(func):
#     def _log(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print("开始……", func.__name__)
#             ret = func(*args, **kwargs)
#             print("结束……", func.__name__)
#             return ret
#
#         return wrapper
#
#     return _log
#
#
# # @log("module")
# def test1(s):
#     print("test1 ..", s)
#     return s
#
#
# # @log("module")    # 相当于 test2 = log(test2)
# def test2(s1, s2):
#     print("test2..", s1, s2)
#     return s1, s2
#
#
# test3 = log(test1("43") )
#
#
# test1("a")
# # print(test3)

import time

current_user = {
    'username': None,
    # 'login_time':None
}


def auth(func):
    func = index
    def wrapper(*args, **kwargs):
        if current_user['username']:
            print('已经登录过了')
            res = func(*args, **kwargs)
            return res

        uname = input('输入用户名：').strip()
        pwd = input('密码：').strip()
        if uname == 'yuan' and pwd == '123':
            print('登录成功')
            current_user['username'] = uname
            res = func(*args, **kwargs)
            return res
        else:
            print('用户名或密码错误')

    return wrapper


@auth
def index():
    time.sleep(0.1)
    print('welcom to index page')


# @auth
def home(name):
    time.sleep(2)
    print('welcome %s to home page' % name)


b = auth(home("yuan"))
print(type(b))

# index()
# input("请输入你的值：")
# home('yuan')
