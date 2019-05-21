# -*-encoding:UTF-8-*-

"""  
读取json文件
"""

""" import json
import csv

json_str = '{"name": "罗浩","age":38,"title":"叫兽"}'
result = json.loads(json_str)
print(result)
print(type(result))
print(result['name'])
print(result['age'])
# 把转换得到的字典作为关键字参数传入Teacher的构造器 """

import json

teacher_dict = {'name': '白元芳', 'age': 25, 'title': '讲师'}
json_str = json.dumps(teacher_dict)
print(json_str)
print(type(json_str))
fruits_list = ['apple', 'orange', 'strawberry', 'banana', 'pitaya']
json_str = json.dumps(fruits_list)
print(json_str)
print(type(json_str))