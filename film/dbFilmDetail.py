#coding:UTF-8
import getDBfilmId
import requests as rs
import re
import os
import json

#   get film  douban  id

# filmId = getDBfilmId.getFilmId('第一滴血')
# print filmId
api = 'http://api.douban.com/v2/movie/subject/'

# print(url+query)

# print getFilmInfo
s = rs.Session()
# r = rs.get(filmListHtml)
# 模拟浏览器的 request 不然 豆瓣 会返回403针对 机器
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}
def getFilmData(filmId):
    getFilmInfo = api + filmId
    q = s.get(getFilmInfo, headers=headers)
    filmData = json.loads(q.text, 'UTF-8')
    return filmData


filmData = getFilmData(str(25662329))
# print type (filmData)
print(filmData)
# print filmData['rating']['average']
# print filmData['images']['small']
# print filmData['title']
# print filmData['ratings_count']