'''
将华氏温度转换为摄氏温度


F = 1.8C +32

'''

# f = float(input("请输入华氏温度:"))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))

"""
输入半径计算圆的周长和面积
"""

# redius = float(input("请输入圆的半径:"))
# perimeter  =  2 * pi * redius
# area = pi * redius * redius
# print('周长: %.2f' % perimeter)
# print('面积 %2.f' % area)

""" 
运算符的使用
"""

from math  import pi
a = 5
b = 10
c = 3
d = 4
e = 5
#a +=b
#a -=c
# a *=
a /= e
#print("a = ", a)


""" flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is not False) """

""" 
字符串常用操作
"""


str1 = "Hello, world!"
print('字符串的长度是:', len(str1))
print('单词首字母大写: ', str1.title())
print('字符串变大写: ', str1.upper())
# str1 = str1.upper()
# print('字符串是不是大写: ', str1.isupper())
# print('字符串是不是以hello开头: ', str1.startswith('hello'))
# print('字符串是不是以hello结尾: ', str1.endswith('hello'))
# print('字符串是不是以感叹号开头: ', str1.startswith('!'))
# print('字符串是不是一感叹号结尾: ', str1.endswith('!'))
str2 = '- \u9a796\u660a'
str3 = str1.title() + ' ' + str2.upper()
print(str3)
