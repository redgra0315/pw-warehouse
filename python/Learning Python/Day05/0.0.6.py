# -*-coding:UTF-8-*-

import time
import math


start = time.perf_counter()
for num in range(1, 1000000):
    sum = 0
    for factor in range(1, int(math.sqrt(num) + 1)):
        if num % factor == 0:
            sum += factor
            if factor > 1 and num / factor != factor:
                sum += num / factor
    if sum == num:
        print(num)
end = time.perf_counter()
print("执行时间:", (end - start), "秒")
