#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "mi"
__mtime__ = "2019/10/21"      
"""

import threading
import time


class MyThread(threading.Thread):

    def run(self):
        print("RUN")
        # return super().run()

    def start(self):
        print("start")
        return super().start()


def worker(n):
    for _ in range(n):
        print("welcome magedu")
        time.sleep(1)


t = MyThread(target=worker, name='worker1', args=(5,))
t.run()
# print("``````````")
# t.run()
# t.start()
