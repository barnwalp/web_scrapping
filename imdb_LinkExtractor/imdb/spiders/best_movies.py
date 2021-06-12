import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


# This spider is inhereting from crawlspider class
class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'

    # adding user-agent through start_requests method
    def start_requests(self):
        yield scrapy.Request(url='http://web.archive.org/web/20200715000935if_/https://www.imdb.com/search/title/?groups=top_250&sort=user_rating', headers={
            'User-Agent': self.user_agent
        })
    # rules is tuple; wherein Rule is an object which tells the crawlspider
    # what are the links you want to follow. In this case you must pass
    # callback method which must not be parse
    # LinkExtractor extract all links which contains 'Items' in the url
    # Instead of allow, you can also pass deny argument which will ensure
    # that specified urls are not extracted
    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(deny=r'Items/'), callback='parse_item', follow=True),
        # you can also use xpath or css to extract link. please note that href
        # argument is not passed as object is capable in extracting links
        # Rule(LinkExtractor(restrict_xpaths=('//a[@class="active"]')), callback='parse_item', follow=True),
        # passing user_agent using set_user_agent method
        Rule(LinkExtractor(restrict_css=('.lister-item-header a')), callback='parse_item', follow=True, process_request='set_user_agent'),
        # order of the Rule objects matter, if following line is placed first, then instead
        # crawling all links in the page first, spider will move on to the next page
        # the reason, call back method was not specified is that after visiting next
        # page, first rule will be called with the callback method
        # Rule(LinkExtractor(restrict_css=('.desc a'))),
        # This is not working because css/xpath selectors are different than the first one
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"), process_request='set_user_agent')
    )

    def set_user_agent(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_test(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item

    def parse_item(self, response):
        yield{
            'title': self.normalize_whitespace(response.css("h1::text").get()),
            'year': response.css("#titleYear a::text").get(),
            'duration': self.normalize_whitespace(response.css("time::text").get()),
            'genre': response.css(".subtext a::text").get(),
            'rating': response.css(".ratingValue span::text").get(),
            'movie_url': response.url,
            # 'user-agent': response.request.headers['User-Agent']
        }
        print(response.url)

    def normalize_whitespace(self, str):
        # removing whitespace from front and tail of string
        str = str.strip()
        # removing unicode chanracter from the strings
        str = str.encode("ascii", "ignore").decode()
        # re.sub replace occurence of particular substring with another
        # substring. In this case occurence of 1 or more whitespce in between
        # words are replaced with one whitespace
        str = re.sub(r'\s+', ' ', str)
        return str
