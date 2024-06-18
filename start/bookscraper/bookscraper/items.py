import scrapy


class BookscraperItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    upc = scrapy.Field()
    stock = scrapy.Field()
