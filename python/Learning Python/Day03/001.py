"""  
身份验证
"""

# username = input("请输入用户名:")
# password = input("请输入密码:")


""" if username == 'admin' and password == '123123':
    print("恭喜你，身份验证成功！")
else:
    print("请重新输入：")
 """

""" x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))
"""
""" 
英制单位英寸和共制单位厘米互换
"""

""" value = float(input('请输入长度: '))
unit = input('请输入单位: ')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print('请输入有效的单位') """


"""  
掷骰子决定做什么事情
"""


# from random import randint
# face = randint(1, 8)
# if face == 1:
#     result = '唱歌'
# elif face == 2:
#     result = '跳舞'
# elif face == 3:
#     result = '蹦迪'
# elif face == 4:
#     result = '睡觉'
# else:
#     result = '讲冷笑话'
# print(result)

"""
输入月收入和五险一金计算个人所得税

"""

salary = float(input('本月收入: '))
insurance = float(input('五险一金: '))
diff = salary - insurance - 3500
if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 1500:
    rate = 0.03
    deduction = 0
elif diff < 4500:
    rate = 0.1
    deduction = 105
elif diff < 9000:
    rate = 0.2
    deduction = 555
elif diff < 35000:
    rate = 0.25
    deduction = 1005
elif diff < 55000:
    rate = 0.3
    deduction = 2755
elif diff < 80000:
    rate = 0.35
    deduction = 5505
else:
    rate = 0.45
    deduction = 13505
tax = abs(diff * rate - deduction)
print('个人所得税: ￥%.2f元' % tax)
print('实际到手收入: ￥%.2f元' % (diff + 3500 - tax))
