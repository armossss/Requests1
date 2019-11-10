# qq空间的爬取
import requests

url_previous = "https://qzone.qq.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
    , "Referer": "http://www.renren.com/972790823/profile"
}
post_data = {"u": "1329272614", "p": "Hjh@Armo16...."}

# session实例化
session = requests.session()
# 将headers和post_data传入
session.post(url_previous, headers=headers, data=post_data)

url_next = "https://user.qzone.qq.com/1329272614/main"
r = requests.get(url_next, headers)
with open("qzone1.html", 'w', encoding='utf-8') as file:  # 为了防止乱码 我们以utf-8的编码打开
    file.write(r.content.decode())


file.close()
