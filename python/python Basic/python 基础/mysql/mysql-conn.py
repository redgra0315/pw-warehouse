#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "mi"
__mtime__ = "2019/10/25"      
"""

import pymysql


def da(n):
    for i in range(n):
        print(i)

# inta = da()
conn = None
try:
    conn = pymysql.connect("192.168.8.161", "testmysql", "123456", "testmysql")


    cousor = conn.cursor()
    sql = "INSERT INTO wx_msg_content VALUES(da(),'bom',52);"
    line = cousor.execute(sql)
    conn.commit()
    print(line)
    cousor.close()
finally:
    if conn:
        conn.close()


