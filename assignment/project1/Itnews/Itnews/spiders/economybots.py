import scrapy
from scrapy.http import Request
from Itnews.items import ItnewsItem
URL = 'https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=101&page=%s'
start_page = 1

def remove_space(title):
    result = []
    for i in range(len(title)):
        if len(title[i].strip()) > 0:
            result.append(title[i].strip())
    
    return result

class EconomybotsSpider(scrapy.Spider):
    name = 'economybots'
    allowed_domains = ['naver.com']
    start_urls = [URL % start_page]

    def start_requests(self):
        for i in range(0, 5):
            yield Request(url=URL % (i+start_page), callback=self.parse)

    def parse(self, response):
        title = response.xpath('//*[@id="main_content"]/div[2]/ul/li/dl/dt[2]/a/text()').extract()
        display = response.css('.lede::text').extract()
        author = response.css('.writing::text').extract()
        new_title = remove_space(title)

        items = []
        for idx in range(len(new_title)):
            item = ItnewsItem()
            item['kind'] = "ECONOMY"
            item['title'] = new_title[idx]
            item['display'] = display[idx]
            item['author'] = author[idx]

            items.append(item)
        return items

