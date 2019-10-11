import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quotespider'

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
            'http://quotes.toscrape.com/page/3/',
            'http://quotes.toscrape.com/page/4/',
            'http://quotes.toscrape.com/page/5/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page_number = response.url.split('/')[-2]
        _file = f'quote_{page_number}.html'
        with open(_file, 'wb') as file:
            file.write(response.body)
