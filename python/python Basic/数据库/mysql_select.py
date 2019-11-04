#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = "yi
__author__ = "mi"
__mtime__ = "2019/11/4"      
"""

import pymysql
from pymysql.cursors import  DictCursor

"""
建立连接
获取游标
执行sql
提交事务
释放资源
"""



def select():
    conn = None
    cursor = None
    # try:
    conn = pymysql.connect("192.168.8.161", "testmysql", "123456", "test")  # ip地址，用户名， 密码， 数据库
    print("数据连接成功")
    cousor = conn.cursor(cursor=DictCursor)  # 获取一个字典类型的Cursor
    sql = "select id from bh_task;"
    line = cousor.execute(sql)  # 操作语句
    print("影响数据的行数为：%d行" % line)
    # print(cursor.fetchone())
    print(cousor.fetchall())
    # print(cousor.fetchone())
    cousor.rownumber=100
    print(cousor.fetchmany(1))

    # except:
    #     conn.rollback()
    #
    # finally:
    #     if conn:
    conn.close()
    #         print("数据连接关闭")


select()
# @create
# def data(num):
#     for i in range(num):
#         sql = "INSERT INTO bh_task VALUES({},'test3','bom','测试任务2')".format(i)
#     return sql
#
#
# for i in range(22):
#     data(i)
