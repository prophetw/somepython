#coding:UTF-8


import requests as rs

s = rs.Session()
#初次打开链接这样可以获得cookies
#下次发送请求 cookies也会被一起发送出去
fir1 = s.get('http://www.baidu.com')

posturl = 'https://passport.baidu.com/v2/api/?login'
postdata = {
'apiver':'v3',
'callback':'parent.bd__pcbs__l7jwqu',
'charset':'UTF-8',
'crypttype':'12',
'detect':'1',
'gid':'20B7A8C-E60F-471B-BA6A-D93972A1465B',
'idc':'',
'isPhone':'false',
'logLoginType':'pc_loginDialog',
'loginmerge':'true',
'logintype':'dialogLogin',
'mem_pass':'on',
'password':'0KR8COFvi6sOhbMA8ORgQl0wI9YbT2/U8KuPx/M7r72XJYhPmUhtk2C5SBFzG++1p0X6xDXrje/L9uEX+HkQRW5yick3n1oS0rVvsTHYRhZJb764FA8/rE34M6+66qEq5lQsT/WyhuCZll/mB+E5Id58PVrS7iD8ggDmqg+lyzk=',
'ppui_logintime':'8320',
'quick_user':'0',
'rsakey':'KmTM5gxV3SStF8nZj20qAzgnlaaRHlWs',
'safeflg':'0',
'splogin':'rate',
'staticpage':'https://www.baidu.com/cache/user/html/v3Jump.html',
'token':'b4861659eefce55524257a3c5b2dd805',
'tpl':'mn',
'tt':'1446290910866',
'u':'https://www.baidu.com/',
'username':'独爱c和弦',
'verifycode':''
}
headers ={
'Host': 'passport.baidu.com',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:41.0) Gecko/20100101 Firefox/41.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Referer': 'https://www.baidu.com/',
'Connection': 'keep-alive'
}

#尝试第一次链接顺便获取验证码

getvalidat = s.post(posturl,data=postdata,headers=headers)
baidu = s.get('http://www.baidu.com')

print baidu.text










