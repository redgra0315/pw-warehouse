#!/usrmeasure=Nonehon
# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "mi"
__mtime__ = "2019/9/26"      
"""

#
# def make_shirt(size, measure, type="shirt"):
#     print("The size of the dress is " +  str(size)  + " small !")
#     print("The size of the dress is:",measure, type)
#
#
# make_shirt(size=37, measure="RED",type="elbow sleeve")

# def describe_city(city_name, state="China"):
#     print(city_name + " is in " + state)
#
#
# describe_city("香港", "中国")
# describe_city("台湾", "中国")
# describe_city("纽约", "美国")

# def get_formatted_name(first_name,last_name):
#     """返回整洁的姓名"""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# musician = get_formatted_name('jami', 'hendrix')
# print(musician)

"""
让实参变成可选的
"""


def get_formatted_name(first_name, middle_name, last_name=' '):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


musi = get_formatted_name('john', 'lee', 'hooker')
print(musi)
