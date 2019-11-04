#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = "使用装饰器来执行MySQL"
__author__ = "mi"
__mtime__ = "2019/11/4"      
"""
import pymysql

"""
建立连接
获取游标
执行sql
提交事务
释放资源
"""
def create(func):
    def wrapper(*args, **kwargs):
        conn = None
        cursor = None
        try:
            conn = pymysql.connect("192.168.8.161", "testmysql", "123456", "test")  # ip地址，用户名， 密码， 数据库
            print("数据连接成功")
            cousor = conn.cursor()  # 游标 Cursor
            # ql = "INSERT INTO bh_task VALUES(3,'test1','bom','测试任务1');"

            # sql = "select * from bh_task;”
            # for i in range(start, num + 1):
            # sql = "INSERT INTO bh_task VALUES({},'test3','bom','测试任务2')".format(i)
            res = func(*args, **kwargs)
            line = cousor.execute(res)  # 操作语句
            print("影响数据的行数为：%d行" % line)
            conn.commit()
        except:
            conn.rollback()

        finally:
            if conn:
                conn.close()
                print("数据连接关闭")

    return wrapper


@create
def data(num):
    for i in range(num):
        sql = "INSERT INTO bh_task VALUES({},'test3','bom','测试任务2')".format(i)
    return sql


for i in range(22):
    data(i)

