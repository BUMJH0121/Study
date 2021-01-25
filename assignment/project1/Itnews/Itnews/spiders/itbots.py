import scrapy
from scrapy.http import Request
from Itnews.items import ItnewsItem
URL = 'https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=105&date=20210125&page=%s'
start_page = 1

def remove_space(title):
    result = []
    for i in range(len(title)):
        if len(title[i].strip()) > 0:
            result.append(title[i].strip())
    
    return result

class ItbotsSpider(scrapy.Spider):
    name = 'itbots'
    allowed_domains = ['naver.com']
    start_urls = [URL % start_page]

    def start_requests(self):
        for i in range(0, 10):
            yield Request(url=URL % (i+start_page), callback=self.parse)

    def parse(self, response):
        title = response.xpath('//*[@id="main_content"]/div[2]/ul[1]/li/dl/dt[2]/a/text()').extract()
        display = response.css('.lede::text').extract()
        author = response.css('.writing::text').extract()
        upload_time = response.css('.date.is_new::text').extract()
        new_title = remove_space(title)

        items = []
        for idx in range(len(title)):
            item = ItnewsItem()
            item['title'] = new_title[idx]
            item['display'] = display[idx]
            item['author'] = author[idx]
            item['upload_time'] = upload_time[idx]

            items.append(item)

            return items