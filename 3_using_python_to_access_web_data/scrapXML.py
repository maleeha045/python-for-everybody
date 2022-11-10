import urllib.request, urllib.parse
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter Location: ")

fh = urllib.request.urlopen(url, context=ctx)
data =fh.read()
tree = ET.fromstring(data)
comment = tree.findall('comments/comment')
count = 0
sum = 0
for com in comment:
    counts = int(com.find("count").text)
    count = count+1
    sum = sum+counts
print("Count:",count)
print("Sum:",sum)
# stuff= ET.fromstring(url)