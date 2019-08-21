# -*- encoding: utf-8 -*-
'''
@File    :   list_3.py
@Time    :   2019/08/21 14:38:02
@Version :   1.0
@Contact :   redgra0315@163.com
@Desc    :   None
'''

# here put the import lib

#定义一个lieb
# data  = []
# # value_name = input("请输入你要插入值：").upper()   #转换为大写
# value_name = input("请输入你要插入值：").title()     #首字母大写其他的小写
# if value_name.isdigit():
#     print("你输入的是数字，我想要字母")
# else:
#     data.append(value_name)
# print(data)



import sys
count = 10 
data  = []
# value_name = input("请输入你要插入值：").upper()   #转换为大写
# value_name = input("请输入你要插入值：").title()     #首字母大写其他的小写
while True:  
    value_name = input("请输入你要插入值：").title().strip()
    if value_name.isdigit():
        print("你输入的是数字，我想要字母")
    # elif value_name.startswith("name"):
    #     print("你第一个想的怎么能是它呢？")
    else:
        data.append(value_name)
        print(data)
        print("请重新输入")

        name = input("是否继续玩下去呢？")
        if name != "n":
            # print(data)
            continue  
    print("你现在写入列表中的值为：%s"  % (data))
    sys.exit(0)