# Scrapy settings for nfl_player project
BOT_NAME = 'spider_name'
SPIDER_MODULES = ['spider_name.spiders']
NEWSPIDER_MODULE = 'spider_name.spiders'
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 3
COOKIES_ENABLED = False

# scrapy-user-agents uses a file with 2200 user-agent strings
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}

# splash setting
SPLASH_URL = 'http://localhost:8050'

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

######################################################
# ----------------------------------------
# SCRAPY PROXY POOL - NOT WORKING
# ----------------------------------------

# DOWNLOADER_MIDDLEWARES = {
#     'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
#     'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
# }
# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'nfl_player.middlewares.NflPlayerDownloaderMiddleware': 543,
#}