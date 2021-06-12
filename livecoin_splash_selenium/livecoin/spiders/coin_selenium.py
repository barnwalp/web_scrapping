import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class CoinSpiderSelnium(scrapy.Spider):
    name = 'coin_selenium'
    start_urls = [
        'https://web.archive.org/web/20200116052415/https://www.livecoin.net/en/'
    ]

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')

        driver = webdriver.Chrome(options=chrome_options)
        # browser shows no of item based on the resolution of the screen
        # since resolution of headless browser is different from the regular
        # browser; it needs to be explicitly specified
        driver.set_window_size(1920, 1080)
        driver.get('https://web.archive.org/web/20200116052415/https://www.livecoin.net/en/')
        rur_tab = driver.find_elements_by_class_name('filterPanelItem___2z5Gb')
        rur_tab[4].click()

        # here html source is a string object; to pass it to parse method
        # it must be converted to a selector object
        self.html = driver.page_source
        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        for currency in resp.css('.ReactVirtualized__Table__row.tableRow___3EtiS'):
            yield{
                'currency_pair': currency.css('.tableRowColumn___rDsl0 div::text').get(),
                'volume(24h)': currency.css('.tableRowColumn___rDsl0:nth-child(2)::text').get()
            }
