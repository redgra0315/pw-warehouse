'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-09-06 17:29:52
@LastEditTime: 2019-09-06 17:29:52
@LastEditors: your name
'''
from urllib  import request,parse

url = "http://www.baidu.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
}

#创建一个hendler

handler = request.HTTPHandler() 

opener = request.build_opener(handler)

request  = request.Request(url,headers=headers)

response  = opener.open(request)
print(response.read().decode())
