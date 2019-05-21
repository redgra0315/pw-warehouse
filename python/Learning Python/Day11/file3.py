# -*-encoding:UTF-8-*-

from math import sqrt


def is_prime(n):
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True


with open('prime-2.txt', 'a') as f:
    # with open('prime-1.txt', 'w') as f:
    for num in range(2, 100):
        if is_prime(num):
            f.write(str(num) + '\n')
print('写入完成！')
