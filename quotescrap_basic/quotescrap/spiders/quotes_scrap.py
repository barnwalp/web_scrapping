import scrapy


# all class inherits from scrapy.Spider class
class QuoteSpider(scrapy.Spider):
    # it identifies the spider and must be unique within a project
    name = 'quote'
    # this url list will be used by the default implementation of
    # start_requests() to create the initial requests for your spider
    # alternatively you may also use start_requests() method
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]
    """
    # Start_requests() must return an iterable of Requests(you can return a
    # list of requests or write a generator function) which the spider will
    # begin to crawl from.

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1',
            'http://quotes.toscrape.com/page/2,
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    """

    # parse is called to handle the response downloaded for each of the
    # requests made. response parameter is an instance of TextResponse that
    # holds the page content. it parses the response.
    def parse(self, response):
        for quote in response.css('.row .col-md-8 .quote'):
            # presence of yield kn a function turns it into a generator; unlike
            # a normal function, generator only runs in response to iteration
            yield{
                'post': quote.css('span.text::text').get(),
                'author': quote.css('.author::text').get(),
                # getting the text from content attributes of the meta class
                # there is also another way which is used in getting next page
                'tags': quote.css('.keywords').attrib['content']
            }
        next_page = response.css('.pager a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            print(f' next page is: {next_page}')
            # callback of a request is a function that be called when reponse
            # of that request is donwloaded; callback func will be called with
            # the downloaded response object as its first argument
            yield scrapy.Request(next_page, callback=self.parse)

        """
        # There is another way to generate requests for the consecutive pages
        # by using response.follow instead of scrapy.Request. unlike scrapy.
        # Request, response.follow supports relative urls directly, however
        # response.follow just return a Request instance; you still have to
        # yield this results. You can also pass the whole anchor tags,
        # response.follow uses their href attribute automatically

        for a in response.css('ul.pager a'):
            yield response.follow(a, callback=self.parse)

        # to create multiple requests for an iterable, you can use
        anchors = response.css('ul.pager a')
        yield from response.follow_all(anchors, callback=self.parse)

        # or shortning it further
        yield from response.follow_all(css='ul.pager a', callback=self.parses)
        """
