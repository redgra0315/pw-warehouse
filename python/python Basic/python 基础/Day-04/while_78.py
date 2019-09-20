#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = "熟食店"
__author__ = "mi"
__mtime__ = "2019/9/19"      
"""

sandwich_orders = ['Meat floss sandwich', 'pastrami', 'Rice sandwich', 'pastrami', 'facade', 'pastrami']
finished_sandwiches = []

#根据列表的索引进行循环
while 'pastrami'  in sandwich_orders:
#for i in sandwich_orders[0:4]:
    print("We're out of spiced beef!")
    name = sandwich_orders.remove('pastrami')
    finished_sandwiches = sandwich_orders[:]
print(finished_sandwiches)

