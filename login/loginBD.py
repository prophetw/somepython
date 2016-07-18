#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests as rs
import re
import hashlib
  
hosturl = 'https://www.baidu.com/'   
posturl = 'https://passport.baidu.com/v2/api/?login'
#get cookies,auto control 当发送请求的时候cookies会被自动发出无需手动设置

s = rs.Session()
firstTouch = s.get(hosturl)
# print firstTouch.cookies


headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
            'Referer': 'https://www.baidu.com/',
	        'Host':'passport.baidu.com',
	        'Connection':'keep-alive',
            'Content-Type':'application/x-www-form-urlencoded'
          }

user = '独爱c和弦'
pwd = 'wangwei891312/'
# pwdEncode
m2 = hashlib.md5()
m2.update(pwd)
print m2.hexdigest()
postData = {
            'username' : user,
            'password' : pwd,
	        'token':'c9491eb87cde07a160f994863bc05a55',
	        'gid':'E7E537E-4278-4416-B25C-EDDB6DFE4F1A'
            }
# print postData
result1 = s.post(posturl,data=postData)
# print result1.cookies