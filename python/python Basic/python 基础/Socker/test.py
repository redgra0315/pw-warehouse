#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = "网络模块学习"
__author__ = "mi"
__mtime__ = "2019/10/24"      
"""

import socket
import time
import threading
import logging

# 定义日志格式
FORMAT = " %(asctime)s [%(levelname)s] %(threadName)s %(funcName)s %(module)s %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt="%Y-%m-%d %H:%M:%S")


class Chatserver():
    def __init__(self, ip="192.168.8.162", port=9999):
        # 定义 ip port
        self.sock = socket.socket()
        self.addr = (ip, port)
        self.event = threading.Event()
        self.clients = {}

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        threading.Thread(target=self._accept(), name="accept").start()

    def stop(self):
        for c in self.clients.values():
            c.close()
        self.sock.close()
        self.event.wait(3)
        self.event.set()

    def _accept(self):
        while not self.event.is_set():
            conn, client = self.sock.accept()
            self.clients[client] = conn  # ip + port
            threading.Thread(target=self._recv, args=(conn,client), name="recv").start()

    def _recv(self, conn,client):
        # 接受数据分发
        while not self.event.is_set():
            data = conn.recv(1024)
            logging.info(data.decode())
            # msg = "ack {}".format(data)
            # 客户端退出机制
            if data == "quit":
                logging.info("qqqqqqqqqqq   quit")
                self.clients.pop(client)
                conn.close()
                break
            msg = "ack {}".format(data)
            for conn in self.clients.values():
                conn.send(msg.encode())


cs = Chatserver()
cs.start()
e = threading.Event()
def show():
    while not e.wait(3):
        logging.info(threading.enumerate())


threading.Thread(target=show, daemon=True).start()

while True:
    cmd = input(">>>>>").strip()
    if cmd == "quit":
        cs.stop()
        break
# 1 TCP SERVER
# sock = socket.socket()  # 1
#
# # 2定义ip和端口
# ip = "192.168.8.162"
# port = 9999
# addr = (ip, port)
# sock.bind(addr)
#
# # 3启动监听
# sock.listen()
#
# # time.sleep(10)
#
#
# conn, addrinfo = sock.accept()  # 默认阻塞的
# logging.info(sock)
# logging.info(addrinfo)
#
# for _ in range(3):
#     # 接收数据
#     data = conn.recv(1024)
#     logging.info(data.decode())
#     msg = "ack {}".format(data.decode())
#     conn.send(msg.encode())

# 释放资源
# sock.close()
