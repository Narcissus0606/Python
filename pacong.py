"""
url="http://192.168.104.1:8080/"
resp=requests.get(url)

print(resp.status_code)
print(resp.encoding)
print(resp.text)

with open("./sut.html","w") as file1:
    file1.write(resp.text)
"""

import requests
url = "http://192.168.104.1:8080/tomcat.png"
resp = requests.get(url)
code = resp.status_code
encode = resp.encoding
data = resp.content
print(code)
print(encode)
print(data)
with open("D:\\workdir\\2019\\07\\09\\tomcat.png","wb") as file:
    file.write(data)
