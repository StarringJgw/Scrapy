import scrapy
from scrapy_splash import SplashRequest
from ..items import CnblogItem
class BlogSpider(scrapy.Spider):
    name="blog"
    start_urls=[
        'https://www.cnblogs.com/pinard/p/000000.html',
    ]
    times=0
    def start_requests(self):
        splash_args = {
            'wait': 1,
        }
        for url in self.start_urls:
            yield SplashRequest(url, self.parse_result, endpoint='render.html',
                                args=splash_args)
    def parse_result(self, response):
        self.times += 1
        self.log(self.times)
        with open(str(self.times)+"."+response.xpath("//title/text()").get()+".html",'wb') as f:
            f.write(("<meta charset='utf-8'>\n"+(response.xpath("//div[@class='post']").get())).encode('utf-8') )

        item=CnblogItem()
        item['number']=self.times
        item['name']=(str(self.times)+"."+response.xpath("//title/text()").get())
        item['link']=response.xpath("//div[@id='post_next_prev']/a[1]/@href").getall()

        yield item
        if self.times==1:
            splash_args = {
                'wait': 1,
            }
            yield SplashRequest(response.xpath("//div[@id='post_next_prev']/a[2]/@href").getall()[0], self.parse_result, endpoint='render.html',
                                args=splash_args)
        elif len(response.xpath("//div[@id='post_next_prev']/a").getall())==4:
            # self.log('loop')
            splash_args = {
                'wait': 1,
            }
            yield SplashRequest(response.xpath("//div[@id='post_next_prev']/a[4]/@href").getall()[0], self.parse_result, endpoint='render.html',
                                args=splash_args)

        # nextUrl=
        # if self.times<5:
