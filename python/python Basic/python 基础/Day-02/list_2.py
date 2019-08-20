#-*- coding:UTF-8 -*-

#列表操作
#1、可以使用 collections 模块的 deque 方法
from collections import deque
# queue = deque(["Eric","John","Michael"])
# queue.append("True")
# print(queue)
# queue.popleft()
# queue.pop()
# print(queue.__sizeof__())
# queue.appendleft("bash")
# print(queue)
# print(queue.maxlen)

#列表推导的三种方法

# sq = []
# for  i in range(10):
#     sq.append(i ** 2)
# print(sq)

# qs = [i ** 2 for i in range(10)]
# print(qs)

# squares = list(map(lambda x: x**2, range(10)))

# print(squares)

#列表中使用嵌套循环与if语句判断


# comb = []
# for x in [1,2,3]:
#     for y in [3,4,5]:
#         if x != y:
#             comb.append((x,y))   #在列表中添加两个值会报错，所以需要在加一个括号括起来
# print(comb)

# #这个方法是上面的那个的升级版

# combs = [(x,y) for x in [1,2,3] for y in [3,4,5] if x != y ]
# print(combs)

# names = [['Tom','Billy','Jef','Andr'],['Alicee','Jill','Ana']]
# for lst in names:
#     for name in lst:
#         if name.count('e') ==2:
#             print("haha")
# print(lst,name)


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
   [9, 10, 11, 12],
]

find = [[row[i] for row in matrix] for i in range(4)]
# print(find)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
# print(transposed)
for row in matrix:
    print("haha")
    print(row)
    print("haha")

