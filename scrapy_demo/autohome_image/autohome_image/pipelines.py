# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request
class AutohomeImagePipeline(object):
    def __init__(self):
        #获取项目下面images文件夹绝对路径
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
        #如果文件件路径不存在则创建
        if not os.path.exists(self.path):
            os.mkdir(self.path)


    def process_item(self, item, spider):
        category = item['category']
        img_urls = item['img_urls']
        category_path = os.path.join(self.path, category)
        #创建类目文件夹
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        for img_url in img_urls:
            img_name = img_url.split('_')[-1]
            request.urlretrieve(img_url, os.path.join(category_path, img_name))
        return item
