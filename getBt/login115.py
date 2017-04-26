#coding:UTF-8

import requests as rs
from bs4 import BeautifulSoup
import re
import os
import datetime
import sys
import string
import random
from hashlib import sha1
import logging
import json

# qrcode 登陆
session = rs.session()
headers = {
'Accept':'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Host':'qrcodeapi.115.com',
'Pragma':'no-cache',
'Referer':'http://qrcodeapi.115.com/bridge_assets.html?cb_key=iframe_cb_key__1487589612513_0&_t1487589612513',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
'X-Requested-With':'XMLHttpRequest'
}
headers1 = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Host':'115.com',
'Pragma':'no-cache',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

firstTouch = session.get('http://115.com/',headers=headers1)
print(firstTouch.cookies.get_dict())
print(session.cookies.get_dict())

tokenUrl='http://qrcodeapi.115.com/api/1.0/web/1.0/token'
token = session.get(tokenUrl,headers=headers)
print(token.text)
print(token.cookies)
dict = json.loads(str(token.text.encode('utf-8')))
print(dict)
keyValue = dict['data']['uid']
header2 ={
'Accept':'image/webp,image/*,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
# 'Host':'passport.115.com',
'Pragma':'no-cache',
'Referer':'http://115.com/',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
loginUrl = 'http://passport.115.com/'
params={
'ct':'login',
'ac':'qrcode',
'key':keyValue,
'v':'',
}
login = session.get(loginUrl,params=params,headers=header2)
print(login.url)
print(login.headers)
print(login.cookies.get_dict())
print(session.cookies.get_dict())



sys.exit()
#

BT_API_URL = 'http://btapi.115.com'
UPLOAD_URL = 'http://upload.115.com'
BASE_URL = 'http://115.com'
PASSPORT_URL = 'http://passport.115.com'
WEB_API_URL = 'http://web.api.115.com'
LOGIN_URL = PASSPORT_URL + '/?ct=login&ac=ajax&is_ssl=1'

def login(username, password):
    # 这混蛋115也是存密码明文
    # 好吧,我们也来生成一个key
    key = string.join(random.sample(['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                                    , 13)).replace(' ', '')
    print('key',key)
    vcode = key.upper()
    session=rs.session()
    password = sha1(sha1(sha1(password).hexdigest() + sha1(username).hexdigest()).hexdigest() + vcode).hexdigest()
    print('password', password)
    data = {'login[ssoent]': 'B1',
            'login[version]': '2.0',
            'login[ssoext]': key,
            'login[ssoln]': username,
            'login[ssopw]': password,
            'login[ssovcode]': key,
            'login[safe]': '1',
            'login[time]': '1',
            'login[safe_login]': '0',
            'login[goto]': 'http://www.115.com/'}
    result = session.post(LOGIN_URL, data)
    print(result.headers)
    print(result.cookies)
    print(session.cookies.get_dict())
    # if not resp['status'] == 200:
    #     logging.error('115登陆失败:请求失败'.decode('utf-8'))
    #     return False
    # ret = json.loads(ret)
    # if 'err_msg' in ret:
    #     logging.error(('115登陆失败:%s' % ret['err_msg'].encode('utf-8')).decode('utf-8'))
    #     return False
    # else:
    #     logging.info('115登陆成功'.decode('utf-8'))
    #     self.get_uid()
    #     return True

login('18119684060','wangwei891312/')





sys.exit()



session = rs.session()
headers={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Host':'www.115.com',
'Pragma':'no-cache',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 115Browser/7.2.4'
}
loginHeaders = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Content-Length':'0',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'OOFL=85475634; UID=85475634_A1_1487520593; CID=8811339dc002f136cc11e069311564a8; SEID=329ff6b3621fb75cf733a9122ba4e66e6e823c5cb076b147df28e1f382559d021113b7f58f73c5608febfc76042cb29e98343edc320dcbb7d4187d8b',
# 'Host':'passport.115.com',
'Origin':'http://115.com',
'Pragma':'no-cache',
'Referer':'http://115.com/',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 115Browser/7.2.4'
}

cookies={
'OOFL':'85475634',
'UID':'85475634_A1_1487520593',
'CID':'8811339dc002f136cc11e069311564a8',
'SEID':'329ff6b3621fb75cf733a9122ba4e66e6e823c5cb076b147df28e1f382559d021113b7f58f73c5608febfc76042cb29e98343edc320dcbb7d4187d8b'
}
session.get('http://115.com/',headers=headers)
session.get('http://www.115.com/',headers=headers)
result = session.post('http://passport.115.com/?ct=login&ac=gotos&goto=http%3A%2F%2F115.com',headers=loginHeaders,cookies=cookies)
print('111')


print(result.status_code)
print(result.headers)
print(session.cookies.get_dict())


final1 = session.get('http://115.com/',headers=loginHeaders)
print(final1.cookies.get_dict())
final2 = session.get('http://home.115.com/home',headers=loginHeaders,cookies=cookies)
print(final1.text)
print(session.cookies.get_dict())

sys.exit()

headers={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Host':'www.115.com',
'Pragma':'no-cache',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 115Browser/7.2.4'
}


class Client115(object):


    __main__=[]

    def __init__(self):
        '''

        '''
        self.headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Cache-Control':'no-cache',
            'Connection':'keep-alive',
            'Host':'www.115.com',
            'Pragma':'no-cache',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 115Browser/7.2.4'
        }
        self.homeUrl = 'http://115.com/'
        self.homeUrl2 = 'http://www.115.com/'
        self.loginUrl = 'http://passport.115.com/?ct=login&ac=gotos&goto=http%3A%2F%2F115.com'
        self.session = rs.session()
        self.cookies = self.loadCookie()



    def login(self):
        '''

        :return:
        '''
        self.stepFirstShakeHand()
    def getLoginInfo(self):
        '''

        :return:
        '''
    def stepFirstShakeHand(self):
        '''

        :return:
        '''

        self.session.get(self.homeUrl,headers=self.headers)
        self.session.get(self.homeUrl2,headers=self.headers)

    def postLoginForm(self):
        '''
        post password username
        :return:
        '''
    def saveCookie(self):
        '''

        :return:
        '''
    def loadCookie(self):
        '''

        :return:
        '''


client = Client115()