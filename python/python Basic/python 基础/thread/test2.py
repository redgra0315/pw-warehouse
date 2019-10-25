#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = "线程锁机制"
__author__ = "mi"
__mtime__ = "2019/10/23"      
"""

import logging
import threading
import time

logging.basicConfig(level=logging.INFO)

cpus = []

lock = threading.Lock()


def worker(lock:threading.Lock, task=100):
    while True:
        lock.acquire()
        count = len(cpus)
        logging.info(count)
        if count >= task:
            lock.release()
            break
        cpus.append(1)
        lock.release()
        logging.info("{} make 1".format(threading.current_thread().name))
    logging.info("{}".format(len(cpus)))


for _ in range(10):
    threading.Thread(target=worker, args=(lock,100)).start()
