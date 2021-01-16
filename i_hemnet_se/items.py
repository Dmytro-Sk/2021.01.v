# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HemnetSeItem(scrapy.Item):
    adress = scrapy.Field()
    price = scrapy.Field()
    square_meters = scrapy.Field()
    # balcony = scrapy.Field()
    city = scrapy.Field()
