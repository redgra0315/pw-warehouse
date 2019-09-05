'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-09-05 16:16:25
@LastEditTime: 2019-09-05 16:45:05
@LastEditors: Please set LastEditors
'''
#!/usr/bin/env  python


#给定一个不超过5位的正整数，判断其有几位（使用input函数）
    #方法一：正常逻辑处理

    # for _ in range(5):
    #     number  = int(input("Please enter a number:"))
    #     if number < 0:
    #         print("Enter is error")
                # break
    #     elif number < 10:
    #         print("The number is one ")
    #     elif number < 100:
    #         print("The number is tuo")
    #     elif number < 1000:
    #         print("The number is three")
    #     elif  number < 10000:
    #         print("The number is four")
    #     else:
    #         print("The number is five")
    # print("accomplish")


#方法二：对折
# for _ in range(5):
#     number = int(input("Please enter a number:"))
#     if number < 0 :
#         print("输入的值错误，请重试！")
#         continue
#     if number > 100:
#         if number > 10000:
#             print("The number is five")
#         elif number > 1000:
#             print("The number is four")
#         else:
#             print("The number is three")
#     else:
#         if  number > 10:
#             print("The number is tuo")
#         else:
#             print("The number is one ")

#方法三：字符串

for _ in range(5):
    number = str(int(input("Please enter a number:")))
    print(len(number))