# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FilmScraperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()


class SerieScraperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    nb_episodes = scrapy.Field()
