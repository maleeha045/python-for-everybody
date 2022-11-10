from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL - ")

############################################### Comment this for first question ##############################
pos = int(input("Enter the position - ")) - 1
count = int(input("Enter the count - "))
count1 = 0
while(count1 < count):

    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    url = tags[pos].get('href')
    name = tags[pos].contents[0]
    count1 = count1 + 1

print(name)