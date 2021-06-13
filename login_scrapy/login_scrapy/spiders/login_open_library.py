import scrapy
from scrapy import FormRequest


class LoginOpenLibrarySpider(scrapy.Spider):
    name = 'login_open_library'
    start_urls = ['https://openlibrary.org/account/login']

    def parse(self, response):
        yield FormRequest.from_response(
            response,
            formcss='#register',
            # redirect, debug_token and login are static data so
            # it can be directly entered in the formdata
            formdata={
                'username': 'suno.pankaj@gmail.com',
                'password': 'test',
                'redirect': '/',
                'debug_token': '',
                'login': 'Log+In',
            },
            callback=self.after_login
        )

    def after_login(self, response):
        if response.css('a[href="/read"]::text').get():
            print('login successful')
