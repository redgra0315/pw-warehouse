#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = "makefile"
__author__ = "mi"
__mtime__ = "2019/10/24"      
"""

import socket
import threading

socketserver = socket.socket()
ip = "0.0.0.0"
port = 9998
addr = (ip, port)
socketserver.bind(addr)
socketserver.listen()
event = threading.Event()

def accept(sock, event: threading.Event):
    s, _ = socketserver.accept()
    f = s.makefile(mode="rw")
    while True:
        line = f.readline()
        print(line)
        if line.strip() == "quit":
            break
        f.write("Return your:{}".format(line))
        f.flush()
    f.close()
    sock.close()
    event.wait(3)
    print("end")
    event.set()


threading.Thread(target=accept, args=(socketserver, event)).start()


while not event.wait(1):
    print(socketserver)




