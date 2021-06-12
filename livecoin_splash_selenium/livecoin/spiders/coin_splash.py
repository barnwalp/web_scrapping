import scrapy
from scrapy_splash import SplashRequest
from scrapy.shell import inspect_response
from scrapy.utils.response import open_in_browser


class CoinSpider(scrapy.Spider):
    name = 'coin'

    script = '''
        function main(splash, args)
          splash.private_mode_enabled = false
          url = args.url
          assert(splash:go(url))
          assert(splash:wait(1))
          rur_tab = assert(splash:select_all(".filterPanelItem___2z5Gb"))
          rur_tab[1]:mouse_click()
          assert(splash:wait(2))
          splash:set_viewport_full()
          return splash:html()
        end
    '''

    def start_requests(self):
        yield SplashRequest(
            url="https://web.archive.org/web/20200116052415/https://www.livecoin.net/en/",
            callback=self.parse,
            endpoint="execute",
            args={
                'lua_source': self.script
            })

    def parse(self, response):
        # This will directly open the response in browser
        # open_in_browser(response)
        # This will open a shell page for further tinkering 
        inspect_response(response, self)
        # for currency in response.css('.ReactVirtualized__Table__row.tableRow___3EtiS'):
        #     yield{
        #         'currency_pair': response.css('.logoBg___2u9Pr::text').get(),
        #         'volume(24h)': response.css('.tableRowColumn___rDsl0:nth-child(2)::text').get()
        #     }
