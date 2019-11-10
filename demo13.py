# 获取豆瓣读书top250榜单 实现翻页爬虫
import requests
import re
from bs4 import BeautifulSoup
# 未完成，由于information函数正则表达式使用不够到位 所以不能很好的提取数据
def get_html_text(url, headers):
    """爬取页面"""
    try:
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()  # 检测是否连接成功，返回状态码为200即为成功，否则抛出异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '失败'


def information(dct, target_html):
    """根据获取到的网页信息，获取需要的数据"""
    soup = BeautifulSoup(target_html,'html.parser')
    a = soup.find_all('a')
    p = soup.find_all('p')
    for i in a:
        try:
            title_string = re.findall(r'.+', target_html)
            dct['key']=title_string
            for j in p:
                try:
                    price_string = re.findall(r'[^/]\d{1, 6}')
                    dct['value'] =price_string
                except:
                    continue
            return dct
        except:
            continue



def print_information(dct):
    """将提取好的信息打印出来，按照设定的格式"""

    table = "{:10}\t\t\{:20}\t\t\t\{:20}"
    print(table.format("序号", "书名", "价格"))
    count = 0  # 计数器
    for k in dct:
        print(table.format(count, k[0], k[1]))




def main():
    url = "https://book.douban.com/top250?icn=index-book250-all"
    headers = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
    result_dct = {}
    target_html = get_html_text(url, headers)
    result = information(result_dct, target_html)
    print_information(result)


main()
