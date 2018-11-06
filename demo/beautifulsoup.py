# beautifulsoup使用 中国天气网爬虫
from bs4 import BeautifulSoup
"""
 find_all使用：
    1.提取标签的时候，第一个参数是标签的名字，第二个参数是标签的属性，可以使用attrs{}过滤多个属性
    2.可以使用limit来限制提取标签的数量
    soup.find_all('a',attrs={"id"="test","class"="ss"},limit=2)
 获取标签的属性
    href = a.attrs['href']
    strings：获取标签下面所有的非标签字符串(内容)，返回的是生成器 
    stripped_strings：跟strings相比，多了去空白字符功能
    get_text：跟strings相比，返回的是普通字符串
 
 select使用
    soup.select('a') 通过标签查找
    soup.select('.class') 通过class查找
    soup.select('#ids') 通过id查找
    soup.select('a #ids') 组合查找 a标签下面id为ids
    soup.select('a[href="ss"]') 属性查找
    
"""

