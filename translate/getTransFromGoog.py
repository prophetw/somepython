import requests
import json



requestsUrl='http://translate.google.cn/translate_a/single'
keywords = 'world'

payload = {
    'client': 't',
    'sl': 'en',
    'tl': 'zh-CN',
    'hl': 'zh-CN',
    'dt': 'at',
    'dt': 'bd',
    'dt': 'ex',
    'dt': 'ld',
    'dt': 'md',
    'dt': 'qca',
    'dt': 'rw',
    'dt': 'rm',
    'dt': 'ss',
    'dt': 't',
    'ie': 'UTF-8',
    'oe': 'UTF-8',
    'otf': '1',
    'srcrom': '0',
    'ssel': '0',
    'tsel': '0',
    'kc': '6',
    'tk': '933927.527245',
    'q': keywords
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}
# result = requests.get(requestsUrl, params=payload, headers=headers)
requestsUrl = 'http://translate.google.cn/translate_a/single?client=t&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&otf=1&srcrom=0&ssel=0&tsel=0&kc=6&tk=933927.527245&q='+keywords
result = requests.get(requestsUrl, headers=headers)
# http://translate.google.cn/translate_a/single?client=t&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&otf=1&srcrom=0&ssel=0&tsel=0&kc=6&tk=933927.527245&q=welcome

arr = [None, None, 123]
print(result.url)
print(result.content)
resultArr = eval('[' + result.content + ']')
#
#
print(resultArr)