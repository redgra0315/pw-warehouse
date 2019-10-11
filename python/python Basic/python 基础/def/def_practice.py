#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = "三个函数的练习"
__author__ = "mi"
__mtime__ = "2019/10/11"      
"""

# def make_shirt(size='大号',style='Python'):
#     # print("这件衣服的样式为 {0},大小为: {1}".format(style,size))
#     print("I LOVE {0} is {1} T 恤".format(style,size))
#
#
# make_shirt(31,'red')
# make_shirt()
# make_shirt("中号","java")
# make_shirt(style="C")

# def describe_city(city,state="China"):
#     print("{0} is in {1}".format(city,state))
#
#
#
# describe_city("Taiwan")
# describe_city("Washington","Washington")
# describe_city("Hongkong")


# 函数返回字典


# def build_person(first_name,last_name,age=""):
#     """返回一个字典，其中包含有关一个人的信息"""
#     person={'first': first_name,'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
# maxd = build_person('jimi','hendix',324)
# print(maxd)


# 城市名
# def city_country(city, state="China"):
#     return city, state
#
#
# # print(len(city_list))
# def build_city(city_list1):
#     list = []
#     for i in range(0, len(city_list1)):
#         city_name = city_list1[i]
#         cist = city_country(city_name)
#         list.append(cist)
#     return list
#
#
# def main():
#     city_list = ['Zhenjiang', 'Jiangxi', 'Guangzhou']
#     hah = build_city(city_list)
#     print(hah, end=" \t")
#
#
# if __name__ == '__main__':
#     main()


# 专辑练习，根据输入专辑的数量来决定循环的次数


album_name = {}


def make_album(name, album, album_count):
    album_name[name] = {"专辑": [album]}, {"歌曲数量": album_count}
    return album_name

while True:
    singer = input("singer is name:")
    album_count = int(input("Please enter the number of albums you want to view:"))
    for i in range(0, album_count):
        song = input("Enter the song you want to listen to:")
        # db_list = album_name[singer][0]['专辑']
        # db_list.append(song)
        if i == 0:
            ha = make_album(singer, song, album_count)
        else:
            db_list = album_name[singer][0]['专辑']
            db_list.append(song)
        # singer
        # album_count += 1
    print(ha)
    exit_status = input("Whether to continue operation(y/n)")
    if exit_status != "y":
        break
# album_name = {'刘德华': ({'专辑': ['练习']}, {'歌曲数量': 2})}
# db_list= album_name[singer][0]['专辑']
# db_list.append("忘情水")
# print(album_name)

