#coding=utf-8
import urllib.request

html=""
def getHtml(url):
	#req.add_header('User-agent', 'Mozilla 5.10')
	res = urllib.request.urlopen(urllib.request.Request(url, headers={'User-agent': 'Mozilla 5.10'}))
	html = res.read()
	return html

try:
	html = getHtml("https://zh.moegirl.org/")

except Exception as e:
	print(e)
else:
	pass
finally:
	pass
# html=getHtml("http://www.baidu.com")
print(html)