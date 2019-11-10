#实例1  爬取京东页面商品信息

import requests

# def getCommodityinfo1():
#     try:
#         r = requests.get("https://item.jd.com/55674461811.html")
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         print(r.text[:1000])
#     except:
#         print("产生异常")
#
#
# getCommodityinfo1()
# print('='*80)

#实例2 ：爬取亚马孙商品信息   修改头部信息
# kv = {'user-agent':'Mozilla/5.0'}
# try:
#     y = requests.get("https://item.jd.com/55674461811.html", headers = kv)
#     y.raise_for_status()
#     y.encoding = y.apparent_encoding
#     print(y.text[:1000])
# except:
#     print("产生异常")

# # 实例3 ：百度搜索和必应搜索关键词提交
# keyword  =  'Python'
# try:
#     p = requests.get("https://www.baidu.com/s", params=keyword)
#     p.raise_for_status()
#     p.encoding = p.apparent_encoding
#     print(p.text[:1000])
# except:
#     print('产生异常')


# 网络图片的爬取与存取

import os
url = "http://img0.dili360.com/pic/2019/09/23/5d88b25b7a1e21g79885614_t.jpg@!rw9"
root = "C:/Users/armo/Desktop/1.jpg"

try:
    k = requests.get(url)
    k.raise_for_status()
    k.encoding = k.apparent_encoding
    f = open(root,'wb')
    f.write(k.content)
    f.close()
except:
    print('爬取失败')

