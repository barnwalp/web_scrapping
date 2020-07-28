import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    start_urls = [
            'http://quotes.toscrape.com/page/1/'
            'http://quotes.toscrape.com/page/2/'
        ]
    """
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/'
            'http://quotes.toscrape.com/page/2/'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    """
    def parse(self, response):
        for quote in response.css('.row .col-md-8 .quote'):
            yield{
                'post': quote.css('span.text::text').get(),
                'author': quote.css('.author::text').get(),
                'tags': quote.css('.keywords').attrib['content']
            }
        # page = response.url.split('/')[-2]
        # filename = 'test-%s.html' % page
        """
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file as %s' % filename)
        """
