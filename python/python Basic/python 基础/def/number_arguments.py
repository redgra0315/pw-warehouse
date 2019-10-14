#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = "传递任意数量的实参"
__author__ = "mi"
__mtime__ = "2019/10/12"      
"""


# def make_pizza(*toppings):
#     """概述要制作的比萨"""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 结合使用位置实参和任意数量实参
# def make_pizza(size, *toppings):
#     """概述要制作的比萨"""
#     print("\nMaking a " + str(size) +
#     "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用任意数量的关键字实参
# def build_profile(first, last, *args, **user_info):
#     """创建一个字典，其中包含我们知道的有关用户的一切"""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     profile['age'] = args
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
#
#
# user_profile = build_profile('albert', 'einstein',
#                              21, 43,
#                              location='princeton',
#                              field='physics')
# print(user_profile)


# 汽车
def make_car(manufacturer, model, **kwargs):
    car_info = {}
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model

    for key, value in kwargs.items():
        car_info[key] = value
    return  car_info

car = make_car('subaru', 'outbcak', color='blue', tow_package='True')
print(car)

