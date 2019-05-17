# -*-coding:UTF-8 -*-

# 文件在linux 执行的时候输入的文件名要加'',例如 '/etc/passwd'
import time
import sys


filename = input('请输入文件名:')
try:
    with open(filename) as f:
        lines = f.readlines()
except FileNotFoundError as msg:
    print('无法打开文件:', filename)
    print(msg)
except UnicodeDecodeError as msg:
    print('文件无法解码')
    sys.exit()
else:
    for line in lines:
        print(line.rstrip())
        time.sleep(0.5)
finally:
    print('不管发生什么都会执行')
