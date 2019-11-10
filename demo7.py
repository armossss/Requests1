# 人人网的爬取
# cookie处理请求

import requests
url_from = "http://www.renren.com/PLogin.do"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
    , "Referer": "http://www.renren.com/972790823/profile"
}
post_data = {"email": "18475882461","password": "gf592152994"}
session = requests.session()  # 实例化session
session.post(url_from, headers=headers, data=post_data)

url_next = "http://www.renren.com/972790823/profile"
r = session.get(url_next, headers=headers)
with open("renren1.html", "w", encoding="utf-8") as file1:
    file1.write(r.content.decode())