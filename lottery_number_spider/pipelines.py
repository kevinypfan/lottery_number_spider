# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class LotteryNumberSpiderPipeline:
    def process_item(self, item, spider):
        return item



class MongoDBPipeline:
    def open_spider(self, spider):
        db_uri = spider.settings.get('MONGODB_URI')
        db_name = spider.settings.get('DATABASE_NAME')
        self.db_client = MongoClient(db_uri)
        self.db = self.db_client[db_name]

    def process_item(self, item, spider):
        self.insert_lottery(item)
        return item

    def insert_lottery(self, item):
        item = dict(item)

        exist_lottery = self.db[item['name_en']].find({'name_en': item['name_en'], 'no': item['no']}).limit(1).count() > 0
        if exist_lottery:
            pass
        else:
            self.db[item['name_en']].insert_one(item)
        

    def close_spider(self, spider):
        self.db_client.close()