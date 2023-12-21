#BeautifulSoup
#引入这个类
#test

from bs4 import BeautifulSoup
import requests
url = "http://192.168.104.1:8080/zh/1.html"
resp = requests.get(url)
html = resp.text
soup = BeautifulSoup(html,"html.parser")
title_list = soup.findAll("title")
print(type(title_list))
for tag in title_list:
    print(tag.get)
