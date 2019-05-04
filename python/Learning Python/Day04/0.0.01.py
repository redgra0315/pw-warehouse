""" 
用for 循环实现1~100求加
"""

sum = 0 
#for x in range(11):
# for x in range(2,11,2):
#     sum += x
#     print(sum)
# print(sum)

for x in range(1,101):
    if x % 2 == 0:
        sum += x
print(sum)