import urllib.request
import urllib.parse

url = "http://456.sszzzz00.com/vod-detail-id-19294.html"
response = urllib.request.urlopen(url)

print(response.read().decode())