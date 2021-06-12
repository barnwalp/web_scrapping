import scrapy
# import logging


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.css("tbody tr")
        for country in countries:
            name = country.css("td a::text").get()
            link = country.css("td a::attr(href)").get()
            next_link = response.urljoin(link)
            # passing the name of country usinig meta argument of Request
            yield scrapy.Request(url=next_link, callback=self.parse_countries, meta={'country_name': name})
            # # instead of urljoin, one can also use response.follow
            # yield response.follow(url=link)

    def parse_countries(self, response):
        name = response.request.meta['country_name']
        table = response.css("table.table.table-striped.table-bordered.table-hover.table-condensed.table-list")[0]
        rows = table.css("tbody tr")
        for row in rows:
            year = row.css("td::text").get()
            population = row.css("td strong::text").get()
            yield{
                'name': name,
                'year': year,
                'population': population
            }
