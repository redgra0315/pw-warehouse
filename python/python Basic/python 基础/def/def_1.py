#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = "函数练习回顾"
__author__ = "mi"
__mtime__ = "2019/10/10"      
"""


# def grest_user(username):
#     print(username + " hana!")
#
#
# grest_user("zairian")


#
# def describe_pet(animal_type, pet_name):
#      """显示宠物的信息"""
#      print("\nI have a " + animal_type + ".")
#      print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
# describe_pet('hamster', 'harry')


# 关键字实参
# def describe_pet(animal_type, pet_name):
#      """显示宠物的信息"""
#      print("\nI have a " + animal_type + ".")
#      print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
# describe_pet( pet_name='harry',animal_type='hamster')

# 默认值
# """使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。 这让Python依然能够正确地解读位置实参。"""
# def describe_pet(pet_name, animal_type='dog'):
#      """显示宠物的信息"""
#      print("\nI have a " + animal_type + ".")
#      print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
# describe_pet('manre')


def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
