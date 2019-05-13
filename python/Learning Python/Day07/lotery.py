# -*-coding:UTF-8-*-

''' 
%d就是普通的输出了
% 2d是将数字按宽度为2，采用右对齐方式输出，若数据位数不到2位，则左边补空格。
% 02d，和% 2d差不多，只不过左边补0
%.2d 输出整形时最少输出2位，如不够前面以0占位。如输出2时变成02。200时只输出200；输出浮点型时（%.2f）小数点后强制2位输出 
'''
from random import randint, randrange, sample


def display(balls):
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print("%02d" % ball, end=' ')
    print()


def random_select():
    red_list = [x for x in range(1, 34)]
    selelcted_balld = []
    for _ in range(6):
        index = randrange(len(red_list))
        selelcted_balld.append(red_list[index])
        print(selelcted_balld)
        del red_list[index]
    selelcted_balld.sort()
    print(selelcted_balld)
    selelcted_balld.append(randint(1, 16))
    print(selelcted_balld)
    return selelcted_balld


def main():
    n = int(input("机选几注："))
    for _ in range(n):
        display(random_select())


if __name__ == "__main__":
    main()
