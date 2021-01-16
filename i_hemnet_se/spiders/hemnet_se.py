import scrapy
from scrapy.crawler import CrawlerProcess
import re
import json

from v_hemnet_se.i_hemnet_se.spiders.locators import Locators
from v_hemnet_se.i_hemnet_se.items import HemnetSeItem


class HemnetSeSpider(scrapy.Spider):
    name = 'hemnet_se'
    start_urls = ['https://www.hemnet.se/bostader?item_types%5B%5D=bostadsratt&keywords=balkong']

    custom_settings = {
        # 'ITEM_PIPELINES': {
        #     'i_simporter.i_simporter.pipelines.ISimporterPipeline': 300
        # },
        # 'FEED_EXPORT_BATCH_ITEM_COUNT': 100,
        'FEED_FORMAT': 'csv',
        'FEED_URI': f"../../iii_results/%(batch_id)02d-{'_'.join(re.findall(r'[A-Z][^A-Z]*', __qualname__)[:-1]).lower()}.csv",
        'FEED_EXPORT_FIELDS': [
            'adress',
            'price',
            'square_meters',
            # 'balcony',
            'city',
        ]
    }

    def parse(self, response, **kwargs):
        data = json.loads(re.search(r'("itemListElement": )(\[.*\])', response.body.decode('utf-8')).group(2))
        for i in list(data):
        # for i in list(data[0:3]):
            url = i['url']

            yield scrapy.Request(url=url, callback=self.parse_item)

        pages_amount = response.xpath(Locators.PAGES_AMOUNT).get()
        for page in range(2, int(pages_amount) + 1):
        # for page in range(2, 3):
            page_url = f'https://www.hemnet.se/bostader?item_types%5B%5D=bostadsratt&keywords=balkong&page={page}'

            yield scrapy.Request(url=page_url, callback=self.parse)

    @staticmethod
    def parse_item(response):
        items = HemnetSeItem()

        # price = re.search(r'("price": )(\d{1,})', response.body.decode('utf-8'), flags=re.S).group(2)
        raw_price1 = response.xpath(Locators.PRICE).get()
        price = ''.join(i for i in re.findall(r'[\d]+', raw_price1))
        adress = response.xpath(Locators.ADRESS).get()
        square_meters = response.xpath(Locators.SQUARE_METERS).get().split(' ')[0]
        # balcony = response.xpath(Locators.BALCONY).get()
        city = response.xpath(Locators.CITY).get()

        items['adress'] = adress
        items['price'] = price
        items['square_meters'] = square_meters
        # items['balcony'] = balcony
        items['city'] = city

        yield items


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(HemnetSeSpider)
    process.start()
