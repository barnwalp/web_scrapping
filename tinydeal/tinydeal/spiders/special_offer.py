import scrapy


class SpecialOfferSpider(scrapy.Spider):
    name = 'special_offer'
    start_urls = ['https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html']

    def parse(self, response):
        for product in response.css(".productListing-even"):
            yield{
                'title': product.css(".p_box_title::text").get(),
                'url': response.urljoin(product.css(".p_box_title::attr(href)").get()),
                'discounted_price': product.css(".productSpecialPrice.fl::text").get(),
                'original_price': product.css(".normalprice.fl::text").get()
            }
