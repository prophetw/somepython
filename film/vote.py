#coding:UTF-8
import requests
import hashlib
import random
import time


md5 = hashlib.md5()

VPath = "http://v4.10brandchina.com/"
itemid = '52056'
brand_id = '52056'
catId = '40374'
authType = '1'

'''
# md5.update('what you want to md5 code')
# md5.hexdigest()   这个是结果
# http://www.10brandchina.com/vote/startin.php?id=40374  投票地址

'''

# rndNum 计算
# rndNum=""+catId + brand_id+Math.round(Math.random()*100000)
random6 = str(int(random.random()*1000000))
rndNum = ""+catId + brand_id + random6
print(rndNum)

# 验证码 图片 获得
# get VPath + "api/captchar.vote.png.php?authType=" + authType + "&rnd=" + rndNum+ "&id=" + brand_id
imgData = {
    'authType': authType,
    'rnd': rndNum,
    'id': brand_id,
}
# imgResponse = requests.get(VPath + "api/captchar.vote.png.php" , params=imgData)
# print(imgResponse.url)
# print(imgResponse.content)
def downloadCapchaImg():
    img = requests.get(VPath + "api/captchar.vote.png.php", params=imgData, stream=True)
    print(img.url)
    with open(rndNum+'.png', 'wb') as fd:
        for chunk in img.iter_content(10):
            fd.write(chunk)
        fd.close()
# downloadCapchaImg()

# capchaValue 是需要自己 去 检查输入的
captchaValue = 'pwyz'


timeSecond = str(int(time.time()))
print(timeSecond)

urlParamStr = "&auth="+authType+"&captcha="+captchaValue+"&catid="+catId+"itemid="+brand_id+"&rnd="+rndNum
sign = hashlib.md5(urlParamStr+timeSecond).hexdigest()
print(sign)

'''
ajaxData('vote',signUrl("itemid="+brand_id+"&catid="+catId+"&captcha="+captchaVal+"&auth="+authType+"&rnd="+rndNum));

function signUrl(queryString) { 
    timestamp=(new Date().getTime().toString().substr(0,10)); 
    strs=queryString.split("&"); 
    strs.sort(); 
    vals=''; 
    for (i=0;i<strs.length;i++) 	{ 
	    vals=vals+strs[i].split("=")[1]; 
	} 
	return queryString+'&sign='+hex_md5(vals+timestamp); }
'''

voteUrl = VPath+'vote/7.do.php'
voteRequestsParams = {
    'itemid':brand_id,
    'catid':catId,
    'auth':authType,
    'captcha':captchaValue,
    'rnd':rndNum,
    'sign':sign
}
val = 'itemid=52056&catid=40374&captcha=pwyz&auth=1&rnd=403745205696139&sign=e6f346b166128cc13fa1743833480397'





