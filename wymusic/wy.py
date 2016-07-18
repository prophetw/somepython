#coding:UTF-8


import requests as rs
import re


s = rs.Session()
r = s.get('http://music.163.com/')
bd = s.get('http://www.baidu.com/')
url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_35847388/?csrf_token='
data = {
'encSecKey':'8e75a56d8e97a8ab3dbf1a66e912d84b936c81e73e9b7c0424517a6d5fe42d8e08f8a0f33bc6c5b6f948e0916c1a4d1c7c1a831ecb22058631d23056b1b3fc759eb323e3990e29272b9b849d043bde5924826076e906276b8e2ce88455db94fd327f8ecc92da0481e1d0e7eb982892f169c5bf8368df42efcecc153f8623c243',
'params':'QDx9fTxsgIV8y00qFUCpBRmBn1auVsY0fC4l7v4YcVF/P7bCpXPfzFVUNPmb/KInBRI9ld8VdAqmqSqI6muhl2c/qj9bzwvTm/AZJMsO8ZmkfVTX5fhIAeWK7au5luPk9uZX5zRHelbZ+YKddSeY+Xg588E9pveWViIXlwYSfrCs1JzVkFpMXrSDJC3P5TC3'
}
headers = {
'Host': 'music.163.com',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:41.0) Gecko/20100101 Firefox/41.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Referer': 'http://music.163.com/song?id=35847388',
'Content-Length': '484',
'Cookie':'JSESSIONID-WYYY=644b2f473cd11e297733e7921c9285e722810affba17a89702fc5973f3fdd95df5ea62d16403c7f32be7040eb097ded575d3b5ffa1d13c50a6a8d096cde6d892dfea12a2332d9ba8c423ea32b5e9c92790a8c2aa71f9b75d764424730543a7dfbe6fead50271e33264dae13a9d46af6d8bbe797e8ac460f22baee09e150e5bb2ed9df091%3A1446273536054; _iuqxldmzr_=25; visited=true; __utma=94650624.619733925.1446271740.1446271740.1446271740.1; __utmb=94650624.8.10.1446271740; __utmc=94650624; __utmz=94650624.1446271740.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
'Connection': 'keep-alive',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache'
}
result = s.post(url,data=data)
print result.text





#print bd.cookies
#print r.cookies
# print result.headers
# print result.text
# print result.encoding


