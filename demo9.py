#  实现 输入文字即可百度翻译

import requests
import json

url = "http://fanyi.baidu.com/basetrans"

query_str = input('请输入你想翻译的文字')

data = {"query": query_str, "from": "zh", "to": "en"}

headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
    , "referer": "https://fanyi.baidu.com/"
    ,"x-requested-with": "XMLHttpRequest"
}

r = requests.post(url, headers=headers, data=data)
html_str = r.content.decode()
print(html_str)
dict_ret = json.loads(html_str)
print('翻译结果是：'+dict_ret["trans"][0]["dst"])

