import scrapy
import json


class ApiQuote(scrapy.Spider):
    name = "apiquote"
    domain_url = 'https://quotes.toscrape.com/api/quotes?page='
    count = 1

    def start_requests(self):
        yield scrapy.Request(
            url='https://quotes.toscrape.com/api/quotes?page=1',
            headers={
                'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
            })

    def parse(self, response):
        data = json.loads(response.body)
        for value in data['quotes']:
            yield{
                'author': value['author']['name'],
                'tag': value['tags'],
                'quote': value['text'],
            }
        # check if the next page is available
        has_next = data['has_next']
        if has_next:
            self.count += 1
            next_link = self.domain_url + str(self.count)
            yield scrapy.Request(url=next_link, callback=self.parse)
