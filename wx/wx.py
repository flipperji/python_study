import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0; SM-G9500 Build/R16NW; wv) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044306 '
                  'Mobile Safari/537.36 MMWEBID/4840 MicroMessenger/6.7.3.1360(0x26070338) '
                  'NetType/WIFI Language/zh_CN Process/toolsmp',
    'Referer': 'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzA5MzI3NjE2MA==&devicetype=android-26&version=26070338&lang=zh_CN&nettype=WIFI&a8scene=7&session_us=gh_15d5aef889d8&pass_ticket=%2BicXaG3uuY2ZVKBllTQgEwF11Gnm002h%2F17RudVsxA8%3D&wx_header=1',
    'Cookie': ' wxuin=216311030; devicetype=android-26; version=26070338; lang=zh_CN; pass_ticket=+icXaG3uuY2ZVKBllTQgEwF11Gnm002h/17RudVsxA8=; wap_sid2=CPbJkmcSXEprMmYyeXV0bTFvX3QzUFFuSFRSdGliWUNjbXRZOWNfdUNFdC13VmhnbWYxbGhWZmgzS3d2TVdiN1c3NkI5UTRFU3lGR2NVRDlPTnMtRjlHaVVfSHlOVURBQUF+MLGgid8FOA1AlU4='
}

params = "action=getmsg&__biz=MzA5MzI3NjE2MA==&f=json&offset=10&count=10&is_ok=1&scene=&uin=777&key=777&pass_ticket=%2BicXaG3uuY2ZVKBllTQgEwF11Gnm002h%2F17RudVsxA8%3D&wxtoken=&appmsg_token=981_LPQrNeepUrP%252FBPWDzz6qdfTVbGoWfHAsgzIfKA~~&x5=1&f=json"
url = "https://mp.weixin.qq.com/mp/profile_ext"

resp = requests.get(url, headers=headers, params=params)
print(resp.content)

