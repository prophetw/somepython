# -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib
import re
import webbrowser

#模拟登录淘宝类
class Taobao:
 
    #初始化方法
    def __init__(self):
        #登录的URL
        self.loginURL = "https://login.taobao.com/member/login.jhtml"
        #代理IP地址，防止自己的IP被封禁
        self.proxyURL = 'http://120.193.146.97:843'
        #登录POST数据时发送的头部信息
        self.loginHeaders =  {
            'Host':'login.taobao.com',
            'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
            'Referer' : 'https://login.taobao.com/member/login.jhtml',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection' : 'Keep-Alive'
        }
        #用户名
        self.username = '独爱弦子'
        #ua字符串，经过淘宝ua算法计算得出，包含了时间戳,浏览器,屏幕分辨率,随机数,鼠标移动,鼠标点击,其实还有键盘输入记录,鼠标移动的记录、点击的记录等等的信息
	self.ua = '078UW5TcyMNYQwiAiwTR3tCf0J/QnhEcUpkMmQ=|Um5OcktySnRAeExzTXBNcCY=|U2xMHDJ+H2QJZwBxX39RaFR6WnQzWjEfSR8=|VGhXd1llXGVdY1dvW2RbZ1JnUG1Pe0R6R31AekJ6Qn5Gfkt1Ww0=|VWldfS0TMwcyBiYaIAAucQBPFD8fIQE9GE4efykZKUBuOG4=|VmNDbUMV|V2NDbUMV|WGRYeCgGZhtmH2VScVI2UT5fORtmD2gCawwuRSJHZAFsCWMOdVYyVTpbPR99HWAFYVMoRSlIM141SBZPCTlZJFkgWnNMdEoBKBcvEFx1SnJNAX8Bf10gSS5ELUpoA2QBKBcvEFxyUnxSBFI=|WWdHFysULAwxES0SKRExBDAOLhItGCUFMA0wECwTJhs7AT0HUQc=|WmZbe1UFMA0zBiZxX2NaY1tlUWldYlxhXGEUKQs0CjAPMwc9AD8GPwQ5BzgBVnhYZzEfSQ==|W2dZeSkHQClCbitzX2NefEB9X2dJaUcASwIuEiYGOxsmBjkGPRNFEw==|XGREFDplPngsVTxGPEIlXjJmWnRUBDEEPx8hGCVzU25OYE5uUWtXaT9p|XWdHFzkXNwsrFC4RJHIk|XmREFDplPngsVTxGPEIlXjJmWnRUaEh3TXNKHEo=|X2dHFzlmPXsvUylEP1kwVThsUH5eDjoHPh4hGy95WWREakRkWmNcZzFn|QHpaCiR7IGYySyJYIlw7QCx4RGpKd1dpUm1YDlg=|QXtbCyV6IWczTzVYI0UsSSRwTGJCfl5gW2JaDFo=|QnpaCiR7IGYySyJYIlw7QCx4RGpKGi8aJwc5ADRiQn9fcV9/Rn9Afyl/|Q3lZCSd4I2UxTTdaIUcuSyZyTmBAfV1kXWRaDFo=|RH5eDiB/JGI2TyZcJlg/RCh8QG5OclJrUmhQBlA=|RXxBfFxhQX5eYltnR3lBe1tjV3dNdVVpVWxMcFBkWHhEfEhoVG1Nc0lpV2xMcExsUmtLdUtrXn5AfFxiXwk='
#密码，在这里不能输入真实密码，淘宝对此密码进行了加密处理，256位，此处为加密后的密码
	self.password2='4fccc50db8f3247b91e91eb301497c0381a14d2487767098bf660269b4f33e62a6805c80393745e872f0574c9f1cdd1b1f6cfc0609f20cdc20787b1b3ab2a67dd5bcf5e30daf2b666947bb9a02418e133e576cf7eaa23c67c6c3fab6922052c5cde5d02179a75e3446ab74447e0667fe77dd0e0865934d32e238989f1aaf895b'
	self.post  = {
            'ua':self.ua,
            'TPL_checkcode':'',
            'CtrlVersion': '1,0,0,7',
            'TPL_password':'',
            'TPL_redirect_url':'http://i.taobao.com/my_taobao.htm?nekot=udm8087E1424147022443',
            'TPL_username':self.username,
            'loginsite':'0',
            'newlogin':'0',
            'from':'tb',
            'fc':'default',
            'style':'default',
            'css_style':'',
            'tid':'XOR_1_000000000000000000000000000000_625C4720470A0A050976770A',
            'support':'000001',
            'loginType':'4',
            'minititle':'',
            'minipara':'',
            'umto':'NaN',
            'pstrong':'3',
            'llnick':'',
            'sign':'',
            'need_sign':'',
            'isIgnore':'',
            'full_redirect':'',
            'popid':'',
            'callback':'',
            'guf':'',
            'not_duplite_str':'',
            'need_user_id':'',
            'poy':'',
            'gvfdcname':'10',
            'gvfdcre':'',
            'from_encoding ':'',
            'sub':'',
            'TPL_password_2':self.password2,
            'loginASR':'1',
            'loginASRSuc':'1',
            'allp':'',
            'oslanguage':'zh-CN',
            'sr':'1280*800',
            'osVer':'macos|10.10',
            'naviVer':'firefox|41'
        }
#将POST的数据进行编码转换
        self.postData = urllib.urlencode(self.post)
        #设置代理
        self.proxy = urllib2.ProxyHandler({'http':self.proxyURL})
        #设置cookie
        self.cookie = cookielib.LWPCookieJar()
        #设置cookie处理器
        self.cookieHandler = urllib2.HTTPCookieProcessor(self.cookie)
        #设置登录时用到的opener，它的open方法相当于urllib2.urlopen
        self.opener = urllib2.build_opener(self.cookieHandler,self.proxy,urllib2.HTTPHandler)

#得到是否需要输入验证码，这次请求的相应有时会不同，有时需要验证有时不需要
    def needIdenCode(self):
        #第一次登录获取验证码尝试，构建request
        request = urllib2.Request(self.loginURL,self.postData,self.loginHeaders)
        #得到第一次登录尝试的相应
        response = self.opener.open(request)
        #获取其中的内容
        content = response.read().decode('gbk')
        #获取状态吗
        status = response.getcode()
        #状态码为200，获取成功
        if status == 200:
            print u"获取请求成功"
            #\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801这六个字是请输入验证码的utf-8编码
            pattern = re.compile(u'\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801',re.S)
            result = re.search(pattern,content)
            #如果找到该字符，代表需要输入验证码
            if result:
                print u"此次安全验证异常，您需要输入验证码"
                return content
            #否则不需要
            else:
                print u"此次安全验证通过，您这次不需要输入验证码"
                return False
        else:
            print u"获取请求失败"
 
#得到验证码图片
    def getIdenCode(self,page):
        #得到验证码的图片
        pattern = re.compile('<img id="J_StandardCode_m.*?data-src="(.*?)"',re.S)
        #匹配的结果
        matchResult = re.search(pattern,page)
        #已经匹配得到内容，并且验证码图片链接不为空
        if matchResult and matchResult.group(1):
            print matchResult.group(1)
            return matchResult.group(1)
        else:
            print u"没有找到验证码内容"
            return False

#程序运行主干
    def main(self):
        #是否需要验证码，是则得到页面内容，不是则返回False
        needResult = self.needIdenCode()
        if not needResult == False:
            print u"您需要手动输入验证码"
            idenCode = self.getIdenCode(needResult)
            #得到了验证码的链接
            if not idenCode == False:
                print u"验证码获取成功"
                print u"请在浏览器中输入您看到的验证码"
                webbrowser.open_new_tab(idenCode)
            #验证码链接为空，无效验证码
            else:
                print u"验证码获取失败，请重试"
        else:
            print u"不需要输入验证码"

taobao = Taobao()
taobao.main()






