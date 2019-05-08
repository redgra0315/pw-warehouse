# -*-coding:UTF-8-*-

from random import randint

connter = 0
answer = randint(0, 10)

while True:
    connter += 1
    number = int(input("请你输入一个数字:"))
    if number < answer:
        print("小了")
    elif number > answer:
        print("大了")
    else:
        print("正好")
        break
print("你总共输入了%d次" % connter)
if connter > 5:
    print("小伙子你没救了")
