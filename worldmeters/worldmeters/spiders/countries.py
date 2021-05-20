import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.css("tbody tr")
        for country in countries:
            name = country.css("td a::text").get()
            link = country.css("td a::attr(href)").get()
            yield{
                'country_name': name,
                'country_link': link
            }
