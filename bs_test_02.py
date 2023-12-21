from bs4 import BeautifulSoup
import requests
#test
url="http://192.168.104.1:8080/zh/2018%E4%B8%AD%E5%9B%BD%E6%9C%80%E5%A5%BD%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D_%E6%9C%80%E5%A5%BD%E5%A4%A7%E5%AD%A6%E7%BD%91.html"
resp = requests.get(url)
resp.encoding = "UTF-8"
html = resp.text
soup = BeautifulSoup(html,"html.parser")

rank_list = soup.select("td:nth-of-type(1)")
school_list = soup.select('td>div')
province_list = soup.select("td:nth-of-type(3)")
score_list = soup.select("td:nth-of-type(4)")

for i in range(0,len(rank_list)-1):
    print(rank_list[i].get_text()+" "+school_list[i].get_text()+" "+province_list[i].get_text()+" "+score_list[i].get_text())

    
