import scrapy
from scrapy.crawler import CrawlerProcess
import csv
import re

from v_hemnet_se.i_hemnet_se.spiders.locators import Locators
from v_hemnet_se.i_hemnet_se.items import HemnetSeItem


class HemnetSeSpider(scrapy.Spider):
    name = 'hemnet_se'
    start_urls = ['https://www.hemnet.se/bostader?item_types%5B%5D=bostadsratt&keywords=balkong']

    custom_settings = {
        'ITEM_PIPELINES': {
            'i_simporter.i_simporter.pipelines.ISimporterPipeline': 300
        },
        'FEED_EXPORT_BATCH_ITEM_COUNT': 100,
        'FEED_FORMAT': 'csv',
        'FEED_URI': f"../../iii_results/%(batch_id)02d-{'_'.join(re.findall(r'[A-Z][^A-Z]*', __qualname__)[:-1]).lower()}.csv",
        'FEED_EXPORT_FIELDS': []
    }

    def parse(self, response, **kwargs):
        items = HemnetSeItem()
        yield items


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(HemnetSeSpider)
    process.start()
