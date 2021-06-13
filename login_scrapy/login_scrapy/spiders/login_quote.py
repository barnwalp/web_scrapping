import scrapy
from scrapy import FormRequest


class LoginQuoteSpider(scrapy.Spider):
    name = 'login_quote'
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        # csrf_token is dynmaically changed each time
        # so it need to be taken from the portal
        csrf_token = response.css('input[name="csrf_token"]::attr(value)').get()
        yield FormRequest.from_response(
            response,
            formcss='form',
            formdata={
                'csrf_token': csrf_token,
                'username': 'admin',
                'password': 'admin',
            },
            callback=self.after_login
        )

    def after_login(self, response):
        if response.css('a[href="/logout"]::text').get():
            print('login successful')
