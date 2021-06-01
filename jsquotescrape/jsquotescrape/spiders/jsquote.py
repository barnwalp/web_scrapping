import scrapy
from scrapy_splash import SplashRequest
from scrapy.shell import inspect_response


class QuoteSpider(scrapy.Spider):
    name = 'jsquote'
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'

    script = """
        function main(splash, args)
          assert(splash:go(args.url))
          assert(splash:wait(1))
          return splash:html()
        end
    """

    def start_requests(self):
        yield SplashRequest(
            url="http://quotes.toscrape.com/js/",
            callback=self.parse,
            endpoint='execute',
            headers={
                'User-Agent': self.user_agent
            },
            args={
                'lua_source': self.script
            })

    def parse(self, response):
        # print(response.request.headers)
        # inspect_response(response, self)
        for quotes in response.css('.quote'):
            yield{
                'quote': quotes.css('.text::text').get(),
                'author': quotes.css('.author::text').get()
            }
        link = response.css('.next a::attr(href)').get()
        next_link = response.urljoin(link)
        if next_link:
            yield SplashRequest(url=next_link,
            callback=self.parse,
            endpoint='execute',
            headers={
                'User-Agent': self.user_agent
            },
            args={
                'lua_source': self.script
            })
