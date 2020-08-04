from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='/home/amjed/chromedriver/chromedriver')

browser.get('https://jasim.tech/automation/one')

time.sleep(1)

name = browser.find_element_by_id('id_name')
name.send_keys('Amjed Saleel')

time.sleep(2)

submit_btn = browser.find_element_by_css_selector('input[type="submit"]')
submit_btn.click()
