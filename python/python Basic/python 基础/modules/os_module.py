#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "mi"
__mtime__ = "2019/10/16"      
"""

# import functools
#
# print(dir(functools))
# print(functools)
# print(functools.wraps)
#
# import os
# print(dir())
# os.path.exists(  )


# import os.path
# import sys
# import test1
#
# print('-----------')
# print((sys.modules['__main__']))
# print(dir())


# import json.encoder
#
# # hh = json.dump()
# print(json.decoder.__dict__)

import sys

print(sorted(sys.modules.keys()))
print(dir())
print(locals()['__package__'])