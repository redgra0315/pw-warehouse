# -*- coding:utf-8 -*-
# 初始化课程名称 subjects、总成绩变量 sum
subjects = ('Python 语言', 'MySQL 数据库', 'Linux 操作系统')
sum = 0
# 重复执行接收考试成绩、求和操作
""" for i in subjects:
    summer = int(input("请输入你的{}成绩:".format(i)))
#   print("请输入{}考试成绩".format(i))
    # 累加成绩
    sum += summer
    print(sum)
# 计算平均值
avg = sum/len(subjects)
# 输出平均成绩
print("王小明的平均成绩是:{}".format(avg))
"""
# while 循环
#i = 1
# 初始化总成绩变量 sum
#sum = 0
j = 1
while j == 2:
    i = 1
    name = input("请输入用户名:")
    print("你好，{}!".format(name))
    sum = 0
# (2) 求平均考试成绩
# -*- coding:utf-8 -*-
# 输入王小明 5 门课程的考试成绩，计算平均值
# 初始化循环计数器 i

# 重复执行 5 次接收考试成绩、求和的操作
    while i <= 5:
        summer = int(input("请输入你的{}成绩:".format(i)))
    # 每门课程计入总成绩
        sum += summer
        i += 1  # 计数器 i 增加 1
# 计算平均值
    avg = sum/(i-1)
# 输出平均成绩
    print("{} 5 门课程的平均成绩是{}".format(name, avg))
#    j += 1
print("学生成绩输入完成！")
== == == =
""" 
用for 循环实现1~100求加
"""

sum = 0
# for x in range(11):
# for x in range(2,11,2):
#     sum += x
#     print(sum)
# print(sum)

for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)