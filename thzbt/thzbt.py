import requests

url = "http://thzbt.co/forum-181-1.html"
headers = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                 ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Referer': 'http://thzbt.co/forum.php'
}
resp = requests.get(url,headers=headers)
print(resp.text)
