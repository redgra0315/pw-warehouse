# -*-coding:UTF-8-*-


def f3(**kw):
    if 'name' in kw:
        print('欢迎你%s!' % 'name')
    elif 'tel' in kw:
        print('你的联系电话是: %s!' % kw['tel'])
    else:
        print('没找到你的个人信息!')


#  **kw 代表的是一个字典
param = {'name': '骆昊', 'age': 38}
f3(**param)
f3(name='骆昊', age=38, tel='13866778899')
f3(user='骆昊', age=38, tel='13866778899')
f3(user='骆昊', age=38, mobile='13866778899')
