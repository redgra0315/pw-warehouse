# -*-coding:UTF-8-*-

''' 
函数的定义和使用 计算组合数c(7,3)
'''


def factorial(n):
    result = 1
    for num in range(1, n+1):
        result *= num
    return result


# print(factorial(7))


def gcd(x, y):
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 1, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1


def lcm(x, y):
    return x * y // gcd(x, y)


print(gcd(27, 15))
print(lcm(15, 27))
