# -*-coding:UTF-8 -*-

'''  
for 循环
'''

#from random import randint
#sum = 0
# for i in range(11):
#    sum += i
# print(sum)
'''  
while 循环
'''

''' from random import randint
anwser = randint(1, 5)

coouter = 0
while True:
    coouter += 1
    number = int(input("请输入"))
    if number < anwser:
        print("大一点")
    elif number > anwser:
        print("小一点")
    else:
        print("恭喜你，终于正确了！")
        continue
        print("asd")
print("你总共猜对了%d次" % coouter)
if coouter > 7:
    print("你智商有问题")
'''

''' 乘法口诀 '''

''' for i in range(1,10):
    for j in range(1, i+1):
        print('%d * %d = %d' % (i ,j, i *j), end='\t')
    print() '''

''' 判断是不是素数 '''


''' from math import sqrt
num = int(input("请输入一个数:"))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and sum != 1:
    print("%d是素数" % num)
else:
    print("%d不是素数" % num)
 '''


''' 输入两个正整数计算最大公约数和最小公倍数

x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公约数是%d' % (x, y, x * y // factor))
        break
'''

'''
三角形
'''
row = int(input('请输入行数: '))
# for i in range(row):
#     for b in range( i + 1):
#         print('*', end='')
#     print()


# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(j)
#             print(i)
#             print('---')
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()

''' for i in range(row):
    for b in range(row - i - 1):
        print(' ', end='')
#        print(b)
        print(i)
        print("baa%d" % b)
      for _ in range(2 * i + 1):
        print('*', end='')  
print() '''

''' for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print() '''


''' n = int(input('n = '))
result = 1
for x in range(1, n + 1):
    result *= x
print('%d! = %d' % (n, result)) '''


sum = 0
num = 5
while num <= 100:
    sum += num
    num += 5
print(sum)