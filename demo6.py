import requests

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

query2 = {
"i": "人生苦短",
"from": "AUTO",
"to": "AUTO",
"salt": "15730978174957",
"sign": "23bb0ec764bdab325b184034a3d8b201"
          }
headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "referer": "http://fanyi.youdao.com/"
}
try:
    test2 = requests.post(url, data=query2, headers=headers)
    test2.raise_for_status()
    test2.encoding = test2.apparent_encoding
    print(test2)
    print(test2.content.decode())
except:
    print('爬取失败')
