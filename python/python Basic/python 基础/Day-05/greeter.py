#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "mi"
__mtime__ = "2019/9/26"      
"""


# def build_person(first_name, last_name):
#     """返回一个字典，其中包含有关一个人的信息"""
#     person = first_name + " " + last_name
#     return person.title()
#
#
# while True:
#     print("\n Input tell me your name:")
#     f_name = input("First name:")
#     if f_name == "q":
#         break
#     l_name = input("Last name:")
#     if l_name == "q":
#         break
#     formatted_name = build_person(f_name, l_name)
#     print("\n Hello", formatted_name + "!")

# def greet_users(names):
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)
#
#
# username = ['hannah', 'ty', 'margot']
# greet_users(username)



def print_models(unprinted_designs, completed_models):
    """ 模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
