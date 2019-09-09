'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-09-06 16:53:20
@LastEditTime: 2019-09-06 17:15:50
@LastEditors: Please set LastEditors
'''
import urllib.request
import urllib.parse
import urllib.error

url = "http://www.maodan.com/"

try:
    response = urllib.request.urlopen(url)
    print(response)
except Exception as e:
    print(e)

