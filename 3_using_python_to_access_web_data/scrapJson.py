import urllib.request, urllib.parse
import json

url = input("Enter URL:")

fh = urllib.request.urlopen(url)
data =fh.read()
# data = urllib.parse.urlencode(fh)(

info = json.loads(data)
sum =0
print("Count:",len(info['comments']))
for item in info['comments']:
 count = item['count']
 sum = sum +count
print(sum)
 
