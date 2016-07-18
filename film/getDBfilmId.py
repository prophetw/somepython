#coding:UTF-8
import requests as rs
import re
import json

searchApi = 'https://movie.douban.com/subject_search'
s = rs.Session()
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}

def getId(str):
    print str
    regForId = '\d+'
    result = re.findall(regForId, str)
    # print result
    return result[0]
def getFilmId(query):
    query = query
    payloads = {'search_text':query}
    getFilmInfo = searchApi
    q = s.get(getFilmInfo,params=payloads,headers=headers)
    str = q.text
    regExp = r'https://movie.douban.com/subject/\d*/'
    re3 = re.findall(regExp,str)
    print re3[0]
    searchFilmId = getId(re3[0])
    # print searchFilmId
    return searchFilmId