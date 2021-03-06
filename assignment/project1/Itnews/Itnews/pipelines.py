# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class ItnewsPipeline:
    def __init__(self):
        self.connection = sqlite3.connect('../db.sqlite3')
        self.cursor = self.connection.cursor()
        
    def process_item(self, item, spider):
        if item['title']:
            self.cursor.execute("select * from news_News where title=?", (item['title'],))
            result = self.cursor.fetchone()
            if result:
                print("exist")
            else:
                self.cursor.execute("insert into news_News (kind, title, display, author) values (?, ?, ?, ?)", (item['kind'], item['title'], item['display'], item['author']))
                self.connection.commit()
                print("store")
        
            return item

    def close_spider(self, spider):
        self.connection.close()

class StockPipeline:
    def __init__(self):
        self.connection = sqlite3.connect('../db.sqlite3')
        self.cursor = self.connection.cursor()
        
    def process_item(self, item, spider):
        if item['name']:
            self.cursor.execute("select * from news_News where name=?", (item['name'],))
            result = self.cursor.fetchone()
            if result:
                print("exist")
            else:
                self.cursor.execute("insert into news_News (name, price, open_price, previous_price) values (?, ?, ?, ?)", (item['name'], item['price'], item['open_price'], item['pervious_price']))
                self.connection.commit()
                print("store")
        
            return item

    def close_spider(self, spider):
        self.connection.close()