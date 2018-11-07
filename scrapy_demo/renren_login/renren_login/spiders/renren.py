# -*- coding: utf-8 -*-
# 模拟人人登录
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url = "http://www.renren.com/PLogin.do"
        data = {'email': '970138074@qq.com', 'password': 'pythonspider'}
        # post请求发送表单格式
        request = scrapy.FormRequest(url, formdata=data, callback=self.parse_page)
        yield request


    def parse_page(self,response):
        # 登录个人主页
        url_profile = "http://www.renren.com/443362311/profile"
        request = scrapy.Request(url=url_profile, callback=self.parse_profile)
        yield request


    def parse_profile(self,response):
        with open('profile.html', 'w', encoding='utf-8') as fp:
            fp.write(response.text)
