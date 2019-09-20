#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'mi'
__mtime__ = '2019/9/18'      
"""
alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'yellow', 'points': '10'}
alien_2 = {'color': 'green', 'points': '15'}
alien = [alien_0, alien_1, alien_2]
for i in alien:
    print("Color is value:", i['color'],  "\n" + " points is value:", i['points'])
    # print("points  is  value:", i['points'])






# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }
#
# print("You ordered a" + pizza['crust'] + "-crust pizza " +
#       "with the following toppings:")
# for topping in pizza['toppings']:
#     print("\t" + topping)


# users = {
#     'abstain': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#     },
#     'maurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     }
# }
# for username, user_info in users.items():
#     print("\n User_name: " + username)
#     full_name = user_info['first'] + " " + user_info['last']
#     location = user_info['location']
#     print("\t Full name: " + full_name.title())
#     print("\t Location: " + location.title())
