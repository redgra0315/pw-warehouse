'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-09-09 10:41:09
@LastEditTime: 2019-09-09 18:06:56
@LastEditors: Please set LastEditors
'''
#keyword-only 参数
# def fn(*args,x):
#     print(x) 
#     print(args)

# fn(2,3,x="retest")


#错误的一种写法
# def fn(z,*,y,x):
#     print(x,y)
#     #print(args)

# fn(2,y=3,x="retest")   #  *号之后，普通参数都变成了必须给出的keyword-only参数


def fn(x,y,z=3,*args,m=4,n,**kwargs):
    print(x,y,z,m,n)
    print(args)
    print(kwargs)
fn(1,2,4)


# 可变参数和参数默认值
