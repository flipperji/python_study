# ip代理使用
from urllib import request
url = 'http://httpbin.org/ip'
# 未使用ip代理
response = request.urlopen(url)
print(response.read())
# 使用ip代理
"""
1. 使用ProxyHandler 构建handler
2. 使用handler构建opener
3. 使用opener发送请求
"""
handler = request.ProxyHandler({"http": "115.46.66.241:8123"})
opener = request.build_opener(handler)
res = opener.open(url)
print(res.read())




