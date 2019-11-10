# BeautifuSoup库的使用
import requests
from bs4 import BeautifulSoup


try:
    p = requests.get("http://ncre.neea.edu.cn/")
    p.raise_for_status()
    p.encoding = p. apparent_encoding
    demo = p.text
    print(p.text[:1000])
except:
    print('爬取失败')

print('*'*100)
soup = BeautifulSoup(demo, "html.parser")
print(soup.prettify())
