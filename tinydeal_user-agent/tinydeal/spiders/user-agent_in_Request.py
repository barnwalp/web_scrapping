import scrapy


class SpecialOfferSpider(scrapy.Spider):
    name = 'user-agent_in_Request'
    start_urls = ['https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html']
    # user-agent can also be added in this way
    def start_requests(self):
        yield scrapy.Request(
            url="https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html",
            headers={
                'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
            })

    def parse(self, response):
        for product in response.css(".productListing-even"):
            yield{
                'title': product.css(".p_box_title::text").get(),
                'url': response.urljoin(product.css(".p_box_title::attr(href)").get()),
                'discounted_price': product.css(".productSpecialPrice.fl::text").get(),
                'original_price': product.css(".normalprice.fl::text").get(),
                'user-agent': response.request.headers['User-Agent']
            }

        next_page = response.css(".nextPage::attr(href)").get()
        if next_page is not None:
            url = response.urljoin(next_page)
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                headers={
                    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
                })