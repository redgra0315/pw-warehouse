# -*-coding:UTF-8-*-

import math

for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')


for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d * %d = %d" % (j, i, i * j), end='\t')
    print()
