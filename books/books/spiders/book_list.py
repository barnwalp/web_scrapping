import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookListSpider(CrawlSpider):
    name = 'book_list'

    # adding user-agent through start_requests method
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    def start_requests(self):
        yield scrapy.Request(url='https://books.toscrape.com/', headers={
            'User-Agent': self.user_agent
        })

    rules = (
        Rule(LinkExtractor(restrict_css=('.image_container a')), callback='parse_item', follow=True),
    )

    def set_user_agent(self, request, spider):
        request.headers['User-Agnet'] = self.user_agent
        return request

    def parse_item(self, response):
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        print(response.request.headers['User-Agent'])