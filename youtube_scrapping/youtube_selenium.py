from selenium import webdriver


url = "https://www.youtube.com/c/JohnWatsonRooney/videos?view=0&sort=p&flow=grid"
browser = webdriver.Chrome()
browser.get(url)

videos = browser.find_elements_by_css_selector("#meta.style-scope.ytd-grid-video-renderer")

for video in videos:
    title = video.find_element_by_css_selector("#video-title").text
    views = video.find_element_by_css_selector("#metadata-line .ytd-grid-video-renderer:nth-child(1)").text
    when = video.find_element_by_css_selector("#metadata-line .ytd-grid-video-renderer:nth-child(2)").text
    print(title, views, when)
