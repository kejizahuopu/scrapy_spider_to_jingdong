import scrapy


class TaobaoSpiderSpider(scrapy.Spider):
    name = 'taobao_spider'
    allowed_domains = ['www.taobao.com']
    start_urls = ['http://www.taobao.com/']

    def parse(self, response):
        pass
