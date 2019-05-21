# -*-coding:UTF-8-*-

"从文本文件中读取数据"

import time


def main():
    with open('致像树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    with open('致像树.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    with open('致像树.txt') as f:
        lines = f.readlines()
    print(lines)


if __name__ == "__main__":
    main()
