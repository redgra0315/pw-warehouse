# -*--coding:UTF-8*-


def prinf(name, age=10):
    print("My name is:" + name, "今年"+str(age)+"岁")
    return


# prinf("天天")


def strTolist(str):
    list = []
    for i in str:
        list.append(i)
    print(list)


# strTolist("asdasdasd")

def Function_together(a, b):
    s = 0
    for i in range(a, b+1):
        #print(b)
        s += i
    print("总和为：", s)


#Function_tov  gether(2, 50)
import timeit
b=timeit.default_number
print(b)