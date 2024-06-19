import scrapy
from allocine.items import FilmScraperItem

class BookspiderSpider(scrapy.Spider):
    name = "film_spider"
    allowed_domains = ["allocine.fr"]
    start_urls = ["https://www.allocine.fr/film/meilleurs/"]

    def parse(self, response):
        books = response.xpath('//h2')

        for book in books :
            book_url = book.xpath('./a/@href').get()
            yield response.follow(book_url, callback=self.parse_book)
        

    def parse_book(self, response):

        item = FilmScraperItem()

        item['title'] = response.xpath('//h1/text()').get()

        yield item
        