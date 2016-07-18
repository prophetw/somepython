import urllib

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

html = getHtml("https://www.baidu.com")
print html
