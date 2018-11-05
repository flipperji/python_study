# http.cookiejar 模块
from urllib import request
from http.cookiejar import  CookieJar
from http.cookiejar import MozillaCookieJar

# Cookie保存
cookiejar = MozillaCookieJar('cookie.txt')
#cookiejar.load(ignore_discard=True)
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)
resp = opener.open('http://baidu.com')
cookiejar.save(ignore_discard=True)
