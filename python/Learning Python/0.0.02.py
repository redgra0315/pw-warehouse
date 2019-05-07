"""
使用变量保存数据并进行算术运算

Version: 0.0.02
Author: XXX
"""

a = 321
b = 123
#    print(a + b)
#    print(a - b)
#    print(a * b)
#    print(a / b)
#    print(a // b)
#   print(a % b)
#    print(a ** b)

"""
使用input函数输入
使用int()进行类型转换
用占位符格式化输出的字符串
"""
# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %d' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))

"""
使用type()检查变量的类型
"""
# a = 100
# b = 12.345
# c = 1 + 5j
# d = 'hello, world'
# e = True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

'''
for 循环枚举
'''
# fruis = ['orage', 'grape', 'pitaya', 'blueberry']
# for index, fruit in enumerate(fruis):
#     print(index, ":", fruit)

# 使用生成式生成列表
# data = [7,20,3,15,11]
# result = [num * 3 for num in data if num > 10]
# print(result)

"""
用zip组合键和值来创建字典
"""

keys = ['1001', '2001', '3001']
names = ['罗皓','沈飞', '白远方']
d = dict(zip(keys, names))
print(d)
