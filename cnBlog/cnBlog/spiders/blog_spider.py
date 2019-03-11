import scrapy
from scrapy_splash import SplashRequest
from ..items import CnblogItem
class BlogSpider(scrapy.Spider):
    name="blog"
    start_urls=[
        'https://www.cnblogs.com/pinard/p/5976811.html',
        'https://www.cnblogs.com/pinard/p/5976811.html',
    ]
    times=0
    def start_requests(self):
        splash_args = {
            'wait': 0.5,
        }
        for url in self.start_urls:
            yield SplashRequest(url, self.parse_result, endpoint='render.html',
                                args=splash_args)
    def parse_result(self, response):
        # with open("examplePage.html",'wb') as f:
        #     f.write(response.body)
        self.times+=1
        item=CnblogItem()
        item['link']=response.xpath("//div[@id='post_next_prev']/a[1]/@href").getall()
        yield item
        if self.times<10:
            splash_args = {
                'wait': 0.5,
            }
            yield SplashRequest(response.xpath("//div[@id='post_next_prev']/a[4]/@href").getall()[0], self.parse_result, endpoint='render.html',
                                args=splash_args)
        self.log(self.times)
        # nextUrl=
        # if self.times<5:
