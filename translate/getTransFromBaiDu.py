#/usr/bin/env python
#coding=utf8

import hashlib
import random
import urllib
import requests
import json
import re
import sys


__author__ = 'wang wei'
print (sys.argv)

# 1.选择当前需要a.翻译的语种  b.需要翻译的文件位置
# 2.目标语种 a.确定生成的文件名称 b.后面的版本考虑选择多种语言 同时生成 多个对应语言文件
# 3.需要翻译的批量最好 以特定格式排列 每个需要翻译的短语之间是一个换行最佳

# 具体实现步骤
# 待翻译的文件 每个翻译短语之间 换行
# f=open(path,method)  path 路径 method r read
# while f.readline():
#  f.readline()
# handle translate

# 其实就是 玩 一个翻译的api
# 下面是 百度翻译的api 随便申请下就可以得到
# APP ID: 自己申请
# 密钥: 自己申请
#   http://api.fanyi.baidu.com/api/trans/product/apidoc
# request url   http://api.fanyi.baidu.com/api/trans/vip/translate

# 关于 utf-8 编码 实例  但是因为脚本申明了 是#coding=utf8   utf8 编码 所以不需要手动编码了
str1 = '中国'
utf8 = str1.encode('utf-8')

# print(type(utf8))

# 关于md5 编码 实例
word='hello world'
encodeword=word.encode('utf-8')
m2 = hashlib.md5()
m2.update(encodeword)
# print(m2.hexdigest())

# URL encode
# 由于 url中传递参数 只能是特定字符 不能出现中文  所以 q 这个必须要 url encode
qq='中国'
result=urllib.parse.quote(qq,safe='')
# print(result)   %E4%B8%AD%E5%9B%BD


#////////////////////// real code start from now

# the const argument
appid = '20160423000019433'
secretKey = '7NrX3vsNbtNxnbK8STfX'
requestUrl='http://api.fanyi.baidu.com/api/trans/vip/translate'
# pureQueryStr this func is to format query string not used in this project
def pureQueryStr(queryStrings):
    # 去掉空格 去掉 换行 等分隔符
    return str
def translate(queryStrings,fromLang,toLang):
    # strings="真是的 你不爱我了么？"
    # # q=strings.encode('utf-8')
    # q=strings
    # fromLang='zh'
    # toLang='en'
    q=queryStrings
    fromLang=fromLang
    toLang=toLang
    salt=random.randint(32768, 65536)
    sign = appid+q+str(salt)+secretKey
    encodeSign=sign.encode('utf-8')
    m2 = hashlib.md5()
    m2.update(encodeSign)
    sign = m2.hexdigest()
    arguments='?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    totalUrl=requestUrl+arguments
    r = requests.get(totalUrl)
    return r
def handleTranslate(result,fileToWriteTo):
    result=json.loads(result)
    # print(result['trans_result'])
    translateResult='"'+result['trans_result'][0]['src']+'"  :  "'+result['trans_result'][0]['dst']+'"'+'\n'
    fileToWriteTo.write(translateResult)
    # return result