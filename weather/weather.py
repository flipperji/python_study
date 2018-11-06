# 中国天气网爬虫 使用BeautifulSoup
import requests
from bs4 import BeautifulSoup

BASE_URL = "http://www.weather.com.cn/textFC/%s.shtml"
ALL_DATA = []
def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/70.0.3538.77 Safari/537.36'
        }
    resp = requests.get(url, headers=headers)
    text = resp.content.decode('utf-8')
    soup = BeautifulSoup(text, 'html5lib')
    div = soup.find('div', class_='conMidtab')
    table_list = div.find_all('table')
    for table in table_list:
        tr_list = table.find_all('tr')[2:]
        for index, tr in enumerate(tr_list):
            td_list = tr.find_all('td')
            city_td = td_list[0]
            if index == 0:
                city_td = td_list[1]
            city = list(city_td.stripped_strings)[0]
            min_timp = list(td_list[-2].stripped_strings)[0]
            ALL_DATA.append({'city':city,"min_timp":int(min_timp)})
def spider():
    # url = "http://www.weather.com.cn/textFC/hb.shtml"
    url = "http://www.weather.com.cn/textFC/gat.shtml"
    urls = {
        'hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn', 'gat'
    }
    for url in urls:
        current_url = BASE_URL % (url)
        print(current_url)
        parse_page( BASE_URL % (url))
    # 分析数据 按照温度高低排序
    ALL_DATA.sort(key=lambda data:data['min_timp'])
    print(ALL_DATA)

if __name__ == '__main__':
    spider()


