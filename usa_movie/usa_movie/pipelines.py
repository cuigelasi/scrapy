# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os

class UsaMoviePipeline(object):
    def process_item(self, item, spider):
#        with open("my_meiju.txt",'a') as fp:
#            fp.write(item['name'].encode("utf8") + '\n')

#        with open("my_meiju_url.txt",'a') as fp:
#            fp.write(item['name'] + '\n')

#        with open("my_meiju_download.txt",'a') as fp:
#            fp.write(item['name'] + '\n')
        
        movie_dir = './download/%s/' % (item['name'])
        if not os.path.exists(movie_dir):
            os.makedirs(movie_dir)
            my_meiju_download = movie_dir + ".txt"
            with open(my_meiju_download,'a') as fp:
                fp.write(item['url'] + '\n')

