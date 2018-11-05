# 猫眼 爬取正在上映的电影
import requests
from lxml import etree

url = "https://movie.douban.com/cinema/nowplaying/shanghai/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Referer': 'https://movie.douban.com/'
}
resp = requests.get(url, headers=headers)
text = resp.text
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
liList = ul.xpath("./li")
movies = []
for li in liList:
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    region = li.xpath("@data-region")[0]
    release = li.xpath("@data-release")[0]
    img = li.xpath(".//img/@src")[0]
    movie = {
        'title': title,
        'score': score,
        'region': region,
        'release': release,
        'img': img
    }

    movies.append(movie)
print(movies)