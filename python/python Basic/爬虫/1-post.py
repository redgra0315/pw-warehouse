import urllib.request
import urllib.parse

#获取posturl的地址
post_url = "https://fanyi.baidu.com/sug"
# word = input("请输入查询的单词:")
word = ' key work'
#构建post表单数据
from_data = {
    'kw': word,

}
#构建请求对象

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}

request = urllib.request.Request(url=post_url,headers=headers)
#发生请求

from_data = urllib.parse.urlencode(from_data).encode()
response = urllib.request.urlopen(request,data=from_data)
print(response.read().decode())
