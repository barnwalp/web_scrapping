import scrapy


class PostSpider(scrapy.Spider):
    # name is a string to identify spider
    name = 'posts'

    start_urls = [
        'https://blog.scrapinghub.com/page/1/'
    ]
    # default callback to process donwload responses when their
    # request dont specifies callback

    def parse(self, response):
        for post in response.css('div.post-item'):
            yield{
                'title': post.css('.post-header h2 a::text')[0].get(),
                'date': post.css('.post-header a::text')[1].get(),
                'author': post.css('.post-header a::text')[2].get()
            }
        next_page = response.css('a.next-posts-link::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
