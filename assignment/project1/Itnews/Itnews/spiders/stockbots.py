import scrapy
from scrapy.http import Request
from Itnews.items import StockItem


class StockbotsSpider(scrapy.Spider):
    name = 'stockbots'
    allowed_domains = ['yahoo.com']
    

    def __init__(self, stock='', **kwargs):
        start_urls = ['https://finance.yahoo.com/quote/%s.KS' % stock]
        print(start_urls)
        super().__init__(**kwargs)

    def parse(self, response):
        name = response.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/text()').extract()
        open_price = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[2]/td[2]/span/text()').extract()
        previous_price = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[1]/td[2]/span/text()').extract()
        price = response.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]/text()').extract()
        print(name, open_price, previous_price, price)



# 017670
# 035420