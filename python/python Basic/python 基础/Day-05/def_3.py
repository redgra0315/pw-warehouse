'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-09-06 11:10:20
@LastEditTime: 2019-09-06 15:20:02
@LastEditors: Please set LastEditors
'''
# def add(y,x=4):
#     return x + y 

# b = add(6,10)
# print(b)

#使用一个*符号
# def add(*nums):
#     su = 0 
#     print(type(nums))
#     for i in nums:
#         su += i 
#     print(su)
# add(3,6,9)

#使用两个** 符号

# def  showconfig(**kw):
#     for k,v in kw.items():
#         print( k, "-->", v)


# def  showconfig(username,*args,**kw):
#     print(username)
#     print(args)
#     for k,v in kw.items():
#         print( k, "-->", v)

# #showconfig('test',"127.0.0.1",80,'test')
# showconfig(host="127.0.0.1",port="80",username="test",password="test")

def fn(*args,x,y,**kw):
    print(x)
    print(y)
    print(args)
    print(kw)
fn(3,5,7,9,10,x=1,y="python")
