import urllib.request


url = "http://456.sszzzz00.com/vod-play-id-"  
html = "-src-1-num-1.html"
# filename ="xiaodianying.txx"
for i in range(19200,19250):
    number = url + str(i) + html
    with open('xiaodianying.txt','a+') as fp:
        fp.write(url + str(i) + html + '\n') 
        fp.close()
print("完成")

