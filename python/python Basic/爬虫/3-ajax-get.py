import urllib.request
import urllib.parse

url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&"

page = int(input("请输入第几页的数据："))
number = 20

#构建get参数
data ={
    'start': (page -1)* number,
    'limit': number,
}
query_string = urllib.parse.urlencode(data)

url += query_string
#构建请求对象


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)
print(response.read().decode())
