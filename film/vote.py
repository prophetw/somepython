import requests


VPath = "http://v4.10brandchina.com/"
itemid = 52056
brand_id = 52056
catId = 40374
authType = 1

# 验证码 图片 获得
# get VPath + "api/captchar.vote.png.php?authType=" + authType + "&rnd=" + rndNum+ "&id=" + brand_id
# rndNum 计算
# rndNum=""+catId + brand_id+Math.round(Math.random()*100000)

captchaValue = 'pwyz'
rnd='403745205696139'


val = 'itemid=52056&catid=40374&captcha=pwyz&auth=1&rnd=403745205696139&sign=e6f346b166128cc13fa1743833480397'


voteUrl = VPath+'vote/7.do.php?'
data={
    'itemid':itemid,
    'catid':catId,
    'captcha':captchaValue,
    'rnd':rnd
}



r = requests.get()


