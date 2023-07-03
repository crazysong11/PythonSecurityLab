import scrapy
from scrapy import Selector
from scrapy import Request
from scrapy.http import HtmlResponse

from python_sp.items import PythonSpItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]

    # start_urls = ["https://movie.douban.com/top250"]
    def start_requests(self):
        for page in range(10):
            #负责翻页，一页25个，一共10页
            yield Request(url=f'https://movie.douban.com/top250?start={page * 25}&filter=')

    def parse(self, response: HtmlResponse, **kwargs):
        sel = Selector(response)
        # 获取电影列表
        movie_items = sel.css('#content > div > div.article > ol > li')
        for item in movie_items:
            # 实例化电影item
            movie_item = PythonSpItem()
            movie_item['title'] = item.css('span.title::text').extract_first()
            movie_item['rate'] = item.css('span.rating_num::text').extract_first()
            movie_item['inq'] = item.css('span.inq::text').extract_first()
            yield movie_item
