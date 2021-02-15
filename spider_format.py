import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):
        for quote in response.css('.row .col-md-8 .quote'):
            yield{
                'post': quote.css('span.text::text').get(),
                'author': quote.css('.author::text').get(),
                'tags': quote.css('.keywords').attrib['content']
            }
        next_page = response.css('.pager a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
