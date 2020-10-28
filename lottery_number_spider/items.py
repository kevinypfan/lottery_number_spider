# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LotteryNumberSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # items = ['power', 'mark_38', 'big', 'mark_49', 'today', 'mark_39', 'star_3', 'star_4', 'win_win']
    name_cht = scrapy.Field()
    name_en = scrapy.Field()
    nums = scrapy.Field()
    image = scrapy.Field()
    no = scrapy.Field()
    date = scrapy.Field()
    nums = scrapy.Field()

