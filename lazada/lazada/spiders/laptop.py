import scrapy


class LaptopSpider(scrapy.Spider):
    name = 'laptop'
    # start_urls = ['https://www.zillow.com/homes/Brownsville,-TX_rb/']

    def start_requests(self):
        url = 'https://www.zillow.com/homes/Brownsville,-TX_rb/'
        yield scrapy.Request(url)

    def parse(self, response):
        home_listing = response.css(".list-card-info")
        for listing in home_listing:
            yield{
                'price': listing.css(".list-card-price").get(),
                'address': listing.css(".list-card-addr").get()
            }
