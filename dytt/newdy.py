# 电影天堂最新电影爬取
import requests
from lxml import etree

BASE_URL = "http://www.dytt8.net"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
# http://www.dytt8.net/html/gndy/dyzz/list_23_1.html
url = "http://www.dytt8.net/html/gndy/dyzz/list_23_1.html"
def get_detail_urls(url):
    resp = requests.get(url, headers=HEADERS)
    # 网站编码是以gbk格式编码的，这个需要视不同网站定义
    text = resp.content
    html = etree.HTML(text)
    # 直接获取所有table标签下面的 a标签的 href属性
    hrefs = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url:BASE_URL+url, hrefs)
    return detail_urls

def spider():
    base_url = "http://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
    for x in range(1, 2):
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            # 遍历单个详情页
            parse_detail_page(detail_url)
def parse_detail_page(url):
   resp = requests.get(url)
   text = resp.content.decode('gbk')
   html = etree.HTML(text)
   text = html.xpath("//font[@color='#07519a']/text()")[0]
   print(text)


if __name__ == '__main__':
    spider()
