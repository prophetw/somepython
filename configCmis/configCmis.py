# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests as rs
import re
import json




def calculatePath(userEmail):
    # ww002@mailinator.com return /User_Homes/ww/ma/ww002@mailinator.com/Reading
    lowerEmail = userEmail.lower()
    # http://stackoverflow.com/questions/16720541/python-string-replace-regular-expression
    # import re
    # line = re.sub(r"(?i)^.*interfaceOpDataFile.*$", "interfaceOpDataFile %s" % fileIn, line)
    cleanId = re.sub(r'[^a-zA-Z]', '', lowerEmail)
    result = cleanId[0:2]+'/'+cleanId[2:4]+'/'+lowerEmail
    path = '/User_Homes/' + result + '/Reading'
    return path
def readConfig(env):
    config={}
    with open('config.html', 'r') as outfile:
        total = outfile.read()
        soup = BeautifulSoup(total, 'lxml')
        soup.prettify()
        envElement = soup.find(id=env)
        if envElement == None:
            print('Not A Valid Env: should be docker,vagrant.demo,demo2,product')
            return False
        # print('====config element====')
        # print(envElement)
        config={
            'url':envElement.find(class_='url').get_text(),
            'base-url':envElement.find(class_='base-url').get_text(),
            'auth-api':envElement.find(class_='auth-api').get_text(),
            'cweb-tools-api':envElement.find(class_='cweb-tools-api').get_text(),
            'user-email':envElement.find(class_='user-email').get_text(),
            'password': envElement.find(class_='password').get_text(),
        }
    return config
def signUp(email, password, apiBaseUrl):
    data = {
        'email': email,
        'password': password
    }
    result = rs.post(apiBaseUrl + 'signup', data=data)
    resultDict = json.loads(result.text)
    if (resultDict['ret'] == 0):
        accessToken = resultDict['data']['access_token']
    else:
        print(resultDict)
        print('====sign up failed====')
        return False
    return accessToken
def getAccessToken(email, password, apiBaseUrl):
    print('getAccessToken')
    accessToken=''
    data={
        'email':email,
        'password':password
    }
    try:
        result = rs.post(apiBaseUrl+'access_token', data=data)
        print(result)
        print(result.url)
        print(result.text)
        resultDict = json.loads(result.text)
        if (resultDict['ret'] == 0):
            accessToken = resultDict['data']['access_token']
        else:
            # print(resultDict)
            print('====auto sign up====')
            signUp(email, password, apiBaseUrl)
        return accessToken
    except:
        print('server error can not access to: '+apiBaseUrl)
        return False

def configCmisIndex(env):
    # env demo vagrant docker product
    config = readConfig(env)
    # print(config)
    if config==False:
        return False
    # if config['user-email'] == '':
    #     print('get config failed')
    #     return False
    email = config['user-email']
    password = config['password']
    apiBaseUrl = config['auth-api']
    # print(email)
    # print(password)
    # print(apiBaseUrl)
    accessToken = getAccessToken(email, password, apiBaseUrl)
    print('accessToken is '+str(accessToken))
    if accessToken=='' or accessToken==False:
        print('failed to get token please config by hand')
        return
    print('====configing====')
    with open('index.html', 'r') as outfile:
        with open('./newIndex.html', 'w') as outPutFile:
            total = outfile.read()
            soup = BeautifulSoup(total, 'lxml')
            soup.prettify()
            cmisTag = soup.find('cmis')
            cmisTag['base-url'] = config['base-url']
            cmisTag['url'] = config['url']
            cmisTag['cweb-tools-api'] = config['cweb-tools-api']
            cmisTag['token'] = accessToken
            total += str(cmisTag)
            print(soup)
            outPutFile.write(str(soup))
            print(total)
configCmisIndex('vagrant')




# print(result)
# print(result.text)
# soup = BeautifulSoup(result.text, 'lxml')
# soup.prettify()