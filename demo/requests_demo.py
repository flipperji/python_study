# request使用
import requests

url = "https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false"
datas = {
    'first': 'true',
    'pn': '1',
    'kd': 'python'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
}

# 使用代理池

proxy = {
    'https': '59.110.240.249:8080'
}
resp = requests.get(url, params=datas, headers=headers)



print(resp.json())





