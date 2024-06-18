import scrapy
from bookscraper.items import BookscraperItem


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.xpath('//article[@class="product_pod"]')
        for book in books:
            book_url = book.xpath('./h3/a').attrib['href']
            yield response.follow(book_url, self.parse_book)

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_book(self, response):
        item = BookscraperItem()
        item['title'] = response.xpath('//h1/text()').get()
        item['upc'] = response.xpath('//th[text()="UPC"]/following-sibling::td/text()').get()
        item['price'] = response.xpath("//p[@class='price_color']/text()").get()
        yield item


