import scrapy
from scrapy import Request
from ..items import *
from re import *
from bs4 import BeautifulSoup
class JdSpiderSpider(scrapy.Spider):
    name = 'jd_spider'
    allowed_domains = ['jd.com']
    # MAX_GOODS = 2000
    MAX_PAGE = 200

    DEFAULT_REQUEST_HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
        'cookie': 'https://search.jd.com/s_new.php?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC&pvid=7e845a90327f4387b295e73196b45182&page=2&s=26&scrolling=y&log_id=1634965567912.9058&tpl=1_M&isList=0&show_items=10021232696544,100016777690,100016514918,100021876378,100017048040,10031299389342,100027098836,100023584910,10025621720527,100021782482,100011269283,100011190721,100012292817,100021167332,100021150248,100009464799,100014373843,33950552707,10024913212662,100011431721,100025374022,100016777700,10033909772792,100026163644,100008893805,28206239565,100010022425,100012779151,47878949717,18788509139',
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50",
        'referer': "https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC"
    
    }
    def start_requests(self):
        for page in range(1,self.MAX_PAGE ):
            yield Request(url='https://search.jd.com/Search?keyword=笔记本&page={}'.format(page),
                          headers=self.DEFAULT_REQUEST_HEADERS,callback=self.parse
                          ,meta={"page" : page})
            


            

    def parse(self, response):
        page = response.request.meta['page']
        ids = findall('wids:\'(.+?)\'', response.text)
        if ids != []:
            id_list = ids[0].split(',')
            header = self.DEFAULT_REQUEST_HEADERS.copy()
            header['referer'] =  'https://search.jd.com/Search?keyword=笔记本&page={}'.format(page)
            for id in id_list:
                yield Request(url="https://item.jd.com/{}.html".format(id),
                              callback=self.item,
                              headers=header)
                
    def item( self ,response):
        print(response.text)
        tag = BeautifulSoup(response.text,'html.parser')
        info = tag.find('div',attrs={
            'class':"Ptable"
        })
        print(info)
