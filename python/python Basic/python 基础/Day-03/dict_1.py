#-*- coding:UTF-8 -*-

tel = {"jack":4098, "sape":4139}


list(tel)
sorted(tel)

#使用dict() 创建字典
# dict_1 = dict([('sape',2341),('ghuido',2187),('java',54)])
# print(sorted(dict_1))

#当键是简单字符串时，有时使用关键字参数指定对更容易：

# dict_2 = dict(bash=1002,ghuido=1231,jack=54)
# print(dict_2)



#循环遍历字典   items()方法同时检索密钥和相应的值
# knights = {'gallahad':'the pure','robin':'the brave'}
# for k,v in knights.items():
#     print(k, '-->', v)


# 循环遍历序列时，可以使用该enumerate()函数同时检索位置索引和相应的值。
# for i,v in enumerate(['tic','tac','tae']):
#     print(i, '--->', v)

#要同时循环两个或更多个序列，条目可以与该zip()功能配对。


# uestions = ['name', 'quest', 'favorite color']
# nswers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(uestions, nswers):
#     print("What is your %s? It is %s" %(q,a))

#要反向循环序列,reversed()函数

# for i in reversed(range(1,10,2)):
#     print(i)

#要按排序顺序循环序列，请使用sorted()返回新排序列表的函数，同时保持源不变,使用set(),这是一个集合


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
