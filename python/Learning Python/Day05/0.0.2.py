# -*-coding:UTF-8-*-

a = 0
b = 1
for i in range(20):
    (a,b) = (b,a+b)
    print(a,end=' /')