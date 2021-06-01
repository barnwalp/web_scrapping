import scrapy
from scrapy_splash import SplashRequest
from scrapy.shell import inspect_response


class QuoteSpider(scrapy.Spider):
    name = 'jsquote'

    script = """
        function main(splash, args):
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
            args={
                'lua_source': self.script
            })

    def parse(self, response):
        print(response.request.headers)
        inspect_response(response, self)
