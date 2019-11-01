#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "mi"
__mtime__ = "2019/10/25"      
"""

import socketserver
import threading


class MyHandler(socketserver.BaseRequestHandler):
    def setup(self):
        # super().setup()
        self.event = threading.Event()

    def handle(self):
        # super().handle()
        print(self.server, self.client_address, self.request)
        while not self.event.is_set():
            data = self.request.recv(1024)
            msg = "You msg = {}".format(data.decode()).encode()
            print(msg)
            self.request.send(msg)

addr = ("192.168.8.162", 9999)
server = socketserver.ThreadingTCPServer(addr, MyHandler)

server.serve_forever(1)

server.server_close()
