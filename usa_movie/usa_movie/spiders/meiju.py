# -*- coding: utf-8 -*-
import scrapy
from usa_movie.items import UsaMovieItem
from scrapy.http import Request

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://meijutt.com/new100.html']

    def parse(self, response):
#        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
#        for each_movie in movies:
#            item = UsaMovieItem()
#            item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
#            yield item
        
#        url_datas = response.css('ul li h5 a::attr(href)').extract()
#        for url_data in url_datas:
#            item = UsaMovieItem()
#            name_data = "http://www.meijutt.com" + url_data.encode("utf8")
#            item['name'] = name_data
#            yield item

        url_datas = response.css('ul li h5 a::attr(href)').extract()
        for url in url_datas:
            url_new = "http://www.meijutt.com" + url.encode("utf8")
            yield Request(url=url_new, callback=self.parse2)

    def parse2(self, response):
        movie_names = response.css('div h1::text').extract()
        movie_datas = response.css('ul li p strong a::attr(href)').extract()
        for movie_data in movie_datas:
            item = UsaMovieItem()
            movie_data = movie_data.encode("utf8")
            movie_name = movie_names[0].encode("utf8")
            #movie_name = movie_name.encode("utf8")
            item['name'] = movie_name
            item['url'] = movie_data
            yield item
            

        #pass
