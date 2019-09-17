# -*- coding: utf-8 -*-
# 定义一个空字典

db = {}
# Python DevOps Notes
# 显示菜单内容

prompt = '''
    (N) 注册用户
    (E) 登录用户
    (C) 查看用户
    (Q) 退出
    请选择：
'''
# 接收菜单选项，并执行相关功能
while True:
    choice = input(prompt).strip()[0].lower()
    print("你选的选项是:[{}]".format(choice))
    if choice not in "necq":
        print("无效的选项，请重试。")
    else:
        if choice == "n":
            while True:
                name = input("请输入用户名:")
                # 根据关键字 name 查看字典中是否已存在此键值对
                if name in db:
                    # if db.has_key(name):
                    print("该用户名已经存在，请重试")
                    continue
                else:
                    break
            pwd = input("input your password:")
            # 存账号密码到字典中
            db[name] = pwd
            print("已经存在字典中")
        elif choice == "c":
            if len(db) == 0:
                print("字典位空")
            else:
                print(db)
        elif choice == "e":
            name = input("请输入用户名:")
            pwd = input("请输入密码:")
            password = db.get(name)
            if password == pwd:
                print("登录成功，欢迎回来{}".format(name))
            else:
                print("登录失败，用户名或密码错误。")
        else:
            print("退出")
            break
