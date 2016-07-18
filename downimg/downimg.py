import urllib
import re


def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html
def getImg(html):
	reg = r'src="(.*?\.jpg)" style='
	regImg = re.compile(reg)
	imglist = re.findall(regImg,html)
	print(imglist)
	x = 0
	for imgurl in imglist:
		if x ==  10:
			return	
		else:
			urllib.urlretrieve(imgurl,'%s.jpg' % x)
			x=x+1
url='http://detail.1688.com/offer/40941541671.html?spm=a2615.7691456.0.0.athZHg'
html =  getHtml(url)
#print(html)
getImg(html)
