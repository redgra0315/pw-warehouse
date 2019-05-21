# -*-encoding:UTF-8-*-

"生成器 - 生成器语法"
''' 
seq = [x * x for x in range(10)]
# print(seq)

gen = (x * x for x in range(10))
# print(gen)
for i in gen:
    #    print(i) '''


''' num = 10
gen = (x ** y for x, y in zip(range(1, num), range(num - 1, 0, -1)))
#print(gen)
n = 1
while n < num:
    #print(next(gen))
    n += 1 '''




def fib(num):
    n,a,b = 0,0,1
    while n <  num:
        yield b 
        a , b = b, a+b
        n +=1
for i in fib(20):
    print(i)