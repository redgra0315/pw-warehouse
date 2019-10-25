#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = "学习log模块"
__author__ = "mi"
__mtime__ = "2019/10/23"      
"""

import logging
import  datetime

#定义日志的格式
FORMAT = " %(asctime)s   [%(levelname)s]  %(threadName)s    %(funcName)s  %(module)s %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt="%Y-%m-%d %H:%M:%S",filename="logotype.log")



#输出日志
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

