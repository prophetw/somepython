#coding:UTF-8



import requests as rs
s = rs.Session()
firstTouch = s.get('http://www.zhihu.com/#signin')

#print firstTouch.header
#分析页面知道验证码图片在下面的网址中 方法是get

gifUrl = 'http://www.zhihu.com/captcha.gif?r=1446275767290'
postUrl = 'http://www.zhihu.com/login/email'

validate= '1234'


postdata = {
'_xsrf':'a484a9dcfcd05ed4ad0cb4635219c16e',
'password':'wangwei891312/',
'remember_me':'true',
'captcha':'1234',
'email':'532300391@qq.com'
}

r = s.post(postUrl,data=postdata)
secondTouch = s.get('http://www.zhihu.com/#signin')
print secondTouch.text
#print r.text
