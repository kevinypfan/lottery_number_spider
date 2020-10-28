import scrapy
from bs4 import BeautifulSoup 
from scrapy_splash import SplashRequest
from ..items import LotteryNumberSpiderItem

class NewsSpider(scrapy.Spider):
    name = "loterry_spider"
    start_urls = ['https://fnc.ebc.net.tw/TaiwanLottery/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 10})
    
    def parse(self, response):
        # print()
        bs = BeautifulSoup(response.text, 'html.parser')
        html_array = bs.find_all('div', {'class': 'lottobox'})
        lottery_cht_names = ['威力彩', '38樂合彩', '大樂透', '49樂合彩', '今彩539', '39樂合彩', '3星彩', '4星彩', '雙贏彩']
        lottery_en_names = ['power', 'mark_38', 'big', 'mark_49', 'today', 'mark_39', 'star_3', 'star_4', 'win_win']
        for num, name in enumerate(lottery_en_names, start=0):
            print(num, name)
            items = LotteryNumberSpiderItem()
            if name not in items:
                no, date = html_array[0].select('div.lotto-no')[0].text.replace("\n", "").replace("第", "").replace("期", ",").split(',')
                
                items['name_cht'] = lottery_cht_names[num]
                items['name_en'] = name
                items['nums'] = list()
                items['image'] = html_array[0].select('img')[0]['src']
                items['no'] = no
                items['date'] = date
                
            children = html_array[num].select('ul > li')
            for child in children:
                items['nums'].append(child.text)
            yield(items)
        # soup = BeautifulSoup(response.text, 'lxml')
        # quotes = soup.select('div.lotto-ball ul li.green.text')
        # for q in quotes:
        #     print(q.text)