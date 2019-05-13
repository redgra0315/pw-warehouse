''' 
列表常用操作
- 列表连接
- 获取长度
- 遍历列表
- 列表切片
- 列表排序
- 列表反转
- 查找元素 
'''


''' 
def main():
    fruits = ['grape', '@pple', 'startw', 'waxberry']
    fruits += ['pitaya','pear','mango']
    for fruit in fruits:
        print(fruit.title(), end=' ')
    print()


if __name__ == "__main__":
    main() 
'''


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    # 用range创建数值列表
    list1 = list(range(1, 11))
    print(list1)
    # 生成表达式
    list2 = [x * x for x in range(1, 11)]
    print(list2)
    list3 = [m + n for m in 'ABCDEFG' for n in '12345']
    print(list3)
    print(len(list3))
    # 生成器(节省空间但生成下一个元素时需要花费时间)
    gen = (m + n for m in 'ABCDEFG' for n in '12345')
    print(gen)
    for elem in gen:
        print(elem, end=' ')
    print()
    gen = fib(20)
    print(gen)
    for elem in gen:
        print(elem, end=' ')
    print()


if __name__ == '__main__':
    main()