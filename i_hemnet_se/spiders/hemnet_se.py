import scrapy
from scrapy.crawler import CrawlerProcess
import re
import json

from v_hemnet_se.i_hemnet_se.spiders.locators import Locators
from v_hemnet_se.i_hemnet_se.items import HemnetSeItem


class HemnetSeSpider(scrapy.Spider):
    name = 'hemnet_se'
    start_urls = ['https://www.hemnet.se/bostader?item_types%5B%5D=bostadsratt&keywords=balkong']

    # custom_settings = {
    #     'ITEM_PIPELINES': {
    #         'i_simporter.i_simporter.pipelines.ISimporterPipeline': 300
    #     },
    #     'FEED_EXPORT_BATCH_ITEM_COUNT': 100,
    #     'FEED_FORMAT': 'csv',
    #     'FEED_URI': f"../../iii_results/%(batch_id)02d-{'_'.join(re.findall(r'[A-Z][^A-Z]*', __qualname__)[:-1]).lower()}.csv",
    #     'FEED_EXPORT_FIELDS': [
    #         'adress',
    #         'price',
    #         'square_meters',
    #         'balcony',
    #         'city',
    #     ]
    # }

    def parse(self, response, **kwargs):
        # items = HemnetSeItem()

        raw_data = response.xpath(Locators.DATA).get()
        # data = re.findall(r'\[\{.+\}\]\}\}\]', raw_data)
        data = json.loads(*re.findall(r'\[\{.+\}\]\}\}\]', raw_data))
        with open(f'../../ii_tr/jquery.json', 'w') as n_f:
            json.dump(data, n_f, indent=2)

        # adress = response.xpath(Locators.ADRESS).get()
        # price = response.xpath(Locators.PRICE).get()
        # square_meters = response.xpath(Locators.SQUARE_METERS).get()
        # balcony = response.xpath(Locators.BALCONY).get()
        # city = response.xpath(Locators.CITY).get()
        #
        # items['adress'] = adress
        # items['price'] = price
        # items['square_meters'] = square_meters
        # items['balcony'] = balcony
        # items['city'] = city

        # yield items


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(HemnetSeSpider)
    process.start()
