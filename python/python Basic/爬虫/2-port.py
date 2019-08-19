import urllib.request
import urllib.parse

post_url = "https://fanyi.baidu.com/v2transapi/"
word = "hello world"
form_data = {
    'from': 'en',
    'to': 'zh',
    'query': word,
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '635171.872978',
    'token': '256be2b05c08328e6739fb04f6af9968',
}


headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}

request = urllib.request.Request(url=post_url,headers=headers)

form_data = urllib.parse.urlencode(form_data).encode()

response = urllib.request.urlopen(request,form_data)
print(response.read().decode())