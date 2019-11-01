#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "mi"
__mtime__ = "2019/10/31"      
"""
import sys

sys.setrecursionlimit(1000)  # 递归限制


class Animal:
    x = 123

    def __init__(self, name):
        self._name = name
        self.__age = 10

    def _name(self):
        return self.name

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, value):
        self.__age = value

    def shout(self):
        return "Animal shout"

    @classmethod
    def clsmtd(cls):
        print(cls, cls.__name__)


class Cat(Animal):
    x = "cat"

    def __init__(self, name):
        super().__init__(name)    # 继承
        self._name = "Cat" + name
        self.__age = 20

    def shout(self):
        return "Cat shout"

    @classmethod
    def clsmtd(cls):
        print(cls, cls.__name__)


class Garfield(Cat):
    pass


class Dog(Animal):
    def run(self):
        return "Dog run "


c = Cat("bom")
# print(c.name)
# print(c.__dict__)ct__
print(c.name)
print(c.shout())
print(c._Animal__age)  # 访问私有属性
print(c.__class__.mro())
print(c.__dict__)
print(c.clsmtd.__dict__)
# print(Garfield.__dict__)
# print(Cat.__dict__)
# print(Animal.__dict__)
