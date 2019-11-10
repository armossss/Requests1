# 爬虫通用框架

import requests

def getHTTPText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'

if __name__ == "__main__":
    url = "http://www.bing.com"
    print(getHTTPText(url))