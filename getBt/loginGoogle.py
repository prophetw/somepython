# -*- coding: utf-8 -*-

import requests as rs
from bs4 import BeautifulSoup
import os
import datetime
import sys
import json


class GoogleClient(object):

    '''
        ======
        值得注意的是
            如果是 vpn 登陆的话  因为不常见的ip 很有可能遇到 安全验证电话验证 这个暂时没办法
        ======
        python 登陆 google
        2017 02 18 home
        usage:
        把需要的 cookies 存下来 下次用直接用 如果 不存在需要 运行下 下面的方法

        client = GoogleClient()
        client.login(userAccount,password,reLogin)
        session = client.getSession()

        sys.path[0] 当前目录

    '''
    __attr__=[
        'loginUrl','homeURL','headers'
    ]

    cookieFile = os.path.join(sys.path[0], "cookie")

    def __init__(self):
        os.chdir(sys.path[0])  # 设置脚本所在目录为当前工作目录
        self.loginUrl = 'https://accounts.google.com'
        self.homeURL = "http://www.google.com"
        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "accept-encoding": "gzip, deflate, sdch, br",
            "accept-language": "zh-CN,zh;q=0.8,en;q=0.6",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        }
        self.__session=rs.session()
        self.__session.headers = self.headers
        self.__cookie = self.__loadCookie()
    def getLoginInfo(self):
        '''

        :return:
        '''
        if self.__cookie:
            print('has cookie local use cookie to login in')
            self.__session.cookies.update(self.__cookie)
            result = self.__session.get("https://www.google.com/")
            soup = BeautifulSoup(result.text, "lxml")
            soup.prettify()
            # print(soup)
            usernameEle = soup.find("div", class_="gb_xb")
            if usernameEle==None:
                print('Login failed retry in the browser!')
            else:
                username = usernameEle.getText()
                # username is type unicode need encode
                # username.encode('utf8')
                print("已登陆账号: " + str(username))

        else:
            print("没有找到cookie文件，请调用login方法登录一次！")

    def login(self,username=None,password=None,reLogin=False):
        '''
        错误返回

        成功返回
        :return:
        '''
        if self.__cookie and reLogin==False:
            print('cookie is exist use cookie want re-login execute login(username=your_account,password=your_psw,reLogin=True)')
            self.getLoginInfo()
            return
        print('*' * 20)
        print('Login----')
        print('*' * 20)


        if username==None:
            # username='wangjiawei1312@gmail.com'
            username='wei_wang@foxitsoftware.com'
        if password==None:
            # password='wangwei123/'
            password='P@ssabc123'

        self.stepFirstShakeHand()
        print('login username: '+username)
        self.stepInputAccount(username)
        self.stepInputPassword(username,password)
        self.getLoginInfo()

    def stepFirstShakeHand(self):
        '''
        get cookies
        :return:
        '''
        self.__session.get(self.homeURL,headers=self.headers)
        self.__session.get(self.loginUrl, headers=self.headers)

    def stepInputAccount(self,username):
        '''
        get html then construct form data by input hidden area args
        inputAccountUrl = 'https://accounts.google.com/ServiceLogin?hl=zh-CN&passive=true&continue=https://www.google.com/#identifier'
        :return:
        '''
        inputAccountUrl = 'https://accounts.google.com/ServiceLogin?hl=zh-CN&passive=true&continue=https://www.google.com/#identifier'
        result = self.__session.get(inputAccountUrl, headers=self.headers)
        soup = BeautifulSoup(result.text, 'lxml')
        soup.prettify()
        inputs = soup.find_all('input', type="hidden")
        postAccountData = {}
        for input in inputs:
            postAccountData[input.get('name')] = input.get('value')
        postAccountData['Email'] = username
        postAccountData['pstMsg'] = 1
        postAccountData['requestlocation'] = inputAccountUrl
        # postAccountData['bgresponse'] = '!29il2PlCZFUS7x9n4K9EHnTi6JtoQs8CAAAAkVIAAAASmQFTwsah3__iy4kqYUl8Rqc8d6NJmmEftWArqd9KIW2BeFemJsOLGLbLY6vmgtA3bmpx6ZXe7vvOwLKNEFwr2YSj0xLdA0B0OB8B4vOSOgnP-1pVvlRXFnm1DlhmX2Ppro8oCd6PdAah0125U8k7nFpFjGx6zrM4z1KUNJi9VOdr2vKvnUwSARdQbfqlpflLd76DbHwR-B2yfeL6q8QKFqeMwbRkxcmCaKEGTT0LrZxS8pEuKwyuFScj4aIr1M_mQoEDJ2rM2_ZwXthdDhpAkLTytOJWYs1INs9vBgxCwe0tvCaaBeX6oAEE4AttSe2_AwyXafkmEHEc9TcUT3OnFl42290Xi0KAL1wbDS9-hZxj0eu-ogk2GBVsIwY08HqZTcZkFxtNWz_g4koNRvvTxOfV0DutqId8aCjdj-n55x71Yc_jgCIm5lFvE7yoidjSkm9s8g4-'

        headers = {
            "origin": "https://accounts.google.com",
            "content-type": "application/x-www-form-urlencoded",
            "referer": "https://accounts.google.com/ServiceLogin?hl=zh-CN&passive=true&continue=https://www.google.com/",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        }
        thirdTouch = self.__session.post('https://accounts.google.com/_/signin/v1/lookup', data=postAccountData, headers=headers, cookies=self.__session.cookies.get_dict())
        print(self.__session.cookies.get_dict())

    def stepInputPassword(self,username,password):
        '''
        get html then construct form data by input hidden area args
        :return:
        '''
        inputPasswordUrl = 'https://accounts.google.com/ServiceLogin?hl=zh-CN&passive=true&continue=https://www.google.com/#password'
        getInputPassword = self.__session.get(inputPasswordUrl, headers=self.headers)

        soup = BeautifulSoup(getInputPassword.text, 'lxml')
        soup.prettify()
        inputs = soup.find_all('input', type="hidden")
        postPasswordData = {}
        for input in inputs:
            postPasswordData[input.get('name')] = input.get('value')
        postPasswordData['Email'] = username
        postPasswordData['Passwd'] = password
        postPasswordData['PersistentCookie'] = 'yes'

        headers = {
            "origin": "https://accounts.google.com",
            "Upgrade-Insecure-Requests": "1",
            "content-type": "application/x-www-form-urlencoded",
            "referer": "https://accounts.google.com/ServiceLogin?hl=zh-CN&passive=true&continue=https://www.google.com/",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        }
        forthTouch = self.__session.post('https://accounts.google.com/signin/challenge/sl/password', data=postPasswordData,
                                  headers=headers, cookies=self.__session.cookies.get_dict())
        print('total cookies: ',self.__session.cookies.get_dict())
        self.__saveCookie()


    def __loadCookie(self):
        '''
        读取cookie文件，返回反序列化后的dict对象，没有则返回None
        :return:
        '''
        if os.path.exists(self.cookieFile):
            print("=" * 50)
            with open(self.cookieFile, "r") as f:
                cookie = json.load(f)
                return cookie
        return None

    def __saveCookie(self):
        """
        :return:
        """
        with open(self.cookieFile, "w") as output:
            cookies = self.__session.cookies.get_dict()
            json.dump(cookies, output)
            print("=" * 50)
            print("generate cookie file in current dir ：", self.cookieFile)
    def getSession(self):
        '''
        :return:
        '''
        return self.__session


if __name__ == '__main__':
    clinet = GoogleClient()
    # clinet.login('wei_wang@foxitsoftware.com','P@ssabc123',reLogin=True)
    clinet.login()
    session = clinet.getSession()
    result = session.get('https://analytics.google.com/analytics/web/?hl=zh-CN#report/conversions-goals-overview/a1680467w127442912p131122512/%3F_u.date00%3D20170205%26_u.date01%3D20170211%26overview_goaloption_ALL-graphOptions.compareConcept%3Danalytics.goal1Completions/')
    # https: // analytics.google.com / analytics / web /?hl = zh - CN  # report/conversions-goals-overview/a1680467w127442912p131122512/%3F_u.date00%3D20170201%26_u.date01%3D20170220%26overview_goaloption_ALL-graphOptions.compareConcept%3Danalytics.goal1Completions/
    # https: // analytics.google.com / analytics / web /?hl = zh - CN  # report/conversions-goals-overview/a1680467w127442912p131122512/%3F_u.date00%3D20170205%26_u.date01%3D20170211%26overview_goaloption_ALL-graphOptions.compareConcept%3Danalytics.goal1Completions/


