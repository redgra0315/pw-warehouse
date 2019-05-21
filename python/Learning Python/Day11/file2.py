# -*-encoding:UTF-8-*-


import os


def visit():
    filename = open('passwd')
    for i in filename.readlines():
        with open('test.txt', 'a') as b:
            b.write(i)
    print()


if __name__ == "__main__":
    visit()
