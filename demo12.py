# 获取淘宝搜索页面的信息，提取其中的商品名称和价格
import requests
import re

# 获取搜索页面的信息


def getHtmlText(url, headers):
    """获取淘宝搜索页面"""
    try:
        r = requests.get(url, timeout=20,headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '爬取失败'


def report_information(ist, html):
    """将淘宝搜索页面的信息提取出来"""
    try:
        pricelist = re.findall(r'\"view_price\":\"[\d.]*\"', html)  # 获取商品价格
        namelist = re.findall(r'\"raw_title\":\".*?\"', html)   # 获取商品标题
        for i in range(len(pricelist)):
            price = eval(pricelist[i].split(':')[1])
            name = eval(namelist[i].split(':')[1])
            ist.append([name, price])
    except:
        return '错误'


def printinfolist(ist):
    tableheader = "{:4}\t{:16}\t{:\8}"
    print("{}\t\t{}\t\t{}\t\t".format("序号", "价格", "商品名称"))
    count = 0  # 计数器
    for s in ist:
        count += 1
        print(tableheader.format(count, s[0], s[1]))


def main():
    searchWord = input('请输入你要搜索的商品')
    headers = {"user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
    # 爬取淘宝搜索页面的多少页
    pageDepth = 2
    start_url = "https://s.taobao.com/search?q="+searchWord
    infolist = []
    for i in range(pageDepth):
        try:
            url = start_url+'&s='+str(44*i)
            html = getHtmlText(url)
            report_information(infolist, html)
        except:
            continue
    printinfolist(infolist)


main()
