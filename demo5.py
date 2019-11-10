# 中国大学排名爬取实例
import bs4
import requests
from bs4 import BeautifulSoup


# 1.从网络上获取大学排名网页内容
def getHTMLinfo(url):
    try:
        p = requests.get(url)
        p.raise_for_status()
        p.encoding = p.apparent_encoding
        return p.text
    except:
        return "爬取失败"


# 2.提取网页内容中内容信息到合适的数据结构
def filluniversitList(colllist, html):
    collsoup = BeautifulSoup(html, "html.parser")
    for tr in collsoup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):  # 判断是否是bs4中定义的标签类型
            tds = tr.find_all('td')
            colllist.append([tds[0].string, tds[1].string, tds[2].string, tds[4].string])  # 获取td标签之间的字符串信息


# 3。利用数据结构展示并输出结果
def printResult(colllist, num):
    print("{}\t\t{}\t\t\t\t\t\t\t{}\t\t{}".format("排名", "学校", "地区", "总分"))
    for i in range(num):
        # print(i)
        c = colllist[i]
        print("{:10}\t{:25}\t{:10}{:10}".format(c[0], c[1], c[2], c[3]))


def main():
    collinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html = getHTMLinfo(url)  # 调用getHTMLinfo()方法
    filluniversitList(collinfo, html)
    printResult(collinfo, 548)


main()
