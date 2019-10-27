# coding: utf-8
# Team : Quality Management Center
# Author：Carson
# Date ：2019/10/25 22:10
# Tool ：PyCharm


class Mycalss:
    """
    This is a class
    """

    # x = 123  # 类变量
    # 实例变量是每一个实例自己的变量，是自己独有的；类变量是类的变量，是所有实例共享的属性和方法。

    def __init__(self, name, age):

        self.age = age
        self.name = name

    def foo(self):  # foo 类属性，也是方法
        print(self.name, self.age)


# print(Mycalss)
# print(Mycalss.__name__)
# print(Mycalss.x)
# print(Mycalss.foo)
# print(Mycalss.__doc__)
# print(type(Mycalss))
a = Mycalss("bom", 23)
a.foo()

print(a.__class__.__dict__, a.__class__.__name__)
print(a.__dict__)
print(a.__dict__["age"])