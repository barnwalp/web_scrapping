from selenium import webdriver
from time import sleep


class MyBot:
    def __init__(self):
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(f'user-agent={user_agent}')
        # only below 2 lines are absolutely needed for headless browser
        self.options.headless = True
        self.options.add_argument('--window-size=1920, 1080')
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument('--disable-extensions')
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--no-sandbox")

        self.driver = webdriver.Chrome(
            options=self.options
        )

        self.driver.get("https://google.com")
        self.driver.get_screenshot_as_file("screenshot.png")
        print(self.driver.title)

MyBot()