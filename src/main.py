from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='/home/amjed/chromedriver/chromedriver')

browser.get('https://google.com')

time.sleep(1)

search_input = browser.find_element_by_name('q')
search_input.send_keys('weather now')

time.sleep(2)

search_btn = browser.find_element_by_css_selector('input[type="submit"]')
search_btn.click()

