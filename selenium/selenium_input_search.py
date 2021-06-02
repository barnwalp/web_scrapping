from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(
    options=chrome_options
)

driver.get('https://duckduckgo.com')
assert "DuckDuckGo" in driver.title

search_input = driver.find_element_by_id('search_form_input_homepage')
search_input.send_keys('my user agent')

# search_btn = driver.find_element_by_id('search_button_homepage')
# search_btn.click()
search_input.send_keys(Keys.ENTER)

# driver.get_screenshot_as_file('screenshot.png')
print(driver.page_source)

driver.close()