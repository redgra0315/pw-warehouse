# count = 0 
# for i in range(0,10000,7):
#     print(i)
#     count += 1
#     if count == 20:
#         break

# for i in range(10,0,-1):
#     print(i)
# 
# for i in range(5):
#     print(i)
# else:
#     print("ok")
# for i in range(1,100,2):
#     i += i
# print(i)

# number = float(input("请输入你的成绩:"))
# if number >= 90:
#     print("你的成绩为:A")
# elif  number >= 80 and  number < 89:
#     print("你的成绩为B")
# elif number >= 70 and  number < 79:
#     print("你的成绩为：C")     
# elif number >= 60 and number <69:
#     print("你的成绩为D")
# else: 
#     print("你的成绩为：E") 


# sum = 0 
# for i in range(2,100,2):
#     sum += i
# print(sum)


# b = 'x'
# print((b * 22)  + (' ' * 2))
# for i in range(8):
#     print('x'  +(' ' * 20)    +     'x')
# print((b * 22)  + (' ' * 2))


# 5 的阶乘法
# sum = 0
# mu = 1
# for i in range(1,6):
#     for j in range(1,i+1):
#         mu *= j
#         # print(mu)
#         # print(b)
#     sum += mu
#     mu = 1    
# print(sum)

#判断它是否具有素数




#99 乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d * %d = %d"  % (i,j,i*j),end=" ")
#     print(" ")


#斐波拉契数列
    #递归实现
def fib_recur(n):
  assert n >= 0, "n > 0"
  if n <= 1:
    return n
  return fib_recur(n-1) + fib_recur(n-2)

for i in range(1, 20):
    print(fib_recur(i), end=' ')