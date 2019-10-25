#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = "多线程"
__author__ = "mi"
__mtime__ = "2019/10/21"      
"""

import threading
import logging


logging.basicConfig(level=logging.INFO)


def worker():
    for x in range(100):
        msg = "{} is running".format(threading.current_thread())
        logging.info(msg)
        t = threading.Thread(target=worker, name="worker-{}".format(0), daemon=True)
        t.start()
        t.join()

# for x in range(50):
t = threading.Thread(target=worker, name="worker-{}".format(0),daemon=True)
t.start()
#join 等待

t.join(5)


print("ending")
print(threading.enumerate())
