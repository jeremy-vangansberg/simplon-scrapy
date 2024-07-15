import scrapy
from allocine.items import SerieScraperItem
from allocine.spiders.allocine_spider_movie import FilmSpider

class SeriesSpider(FilmSpider):
    name = "serie_spider"
    allowed_domains = ["allocine.fr"]
    start_urls = ["https://www.allocine.fr/series/top/"]

    def __init__(self, category=None, *args, **kwargs):
        super(FilmSpider, self).__init__(*args, **kwargs)
        self.item = SerieScraperItem()

    def parse(self, response):
        books = response.xpath('//h2')

        for book in books :
            book_url = book.xpath('./a/@href').get()
            yield response.follow(book_url, callback=self.parse_book)
        

    def parse_book(self, response):
        # Consume the generator from the parent class
        film_item_generator = super().parse_book(response)
        film_item = next(film_item_generator)

        # Create an instance of SerieScraperItem
        item = self.item

        # Copy all fields from the film_item to the new item
        for field in film_item.fields:
            item[field] = film_item.get(field)

        # Update item with additional fields or modify existing fields
        item['nb_episodes'] = response.xpath("(//div[@class='stats-item'])[1]")

        yield item

        