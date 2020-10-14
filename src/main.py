from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip

browser = webdriver.Chrome(executable_path='/home/amjed/chromedriver/chromedriver')
browser.maximize_window()

browser.get("https://web.whatsapp.com/")
time.sleep(10)

with open('groups.txt', 'r', encoding='utf8') as f:
    groups = [group.strip() for group in f.readlines()]

with open('msg.txt', 'r', encoding='utf8') as f:
    messages = f.read()

for group in groups:
    search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
    search_box = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, search_xpath))
    )
    
    pyperclip.copy(group)
    search_box.send_keys(Keys.SHIFT, Keys.INSERT)

    time.sleep(2)

    group_title_xpath = f'//span[@title="{group}"]'
    group_title = browser.find_elements_by_xpath(group_title_xpath)

    group_title.click()

    time.sleep(2)

    input_box_xpath = '//div[@@contenteditable="true"][@data-tab="1"]'
    input_box = browser.find_elements_by_xpath(input_box_xpath)

    pyperclip.copy(messages)
    input_box.send_keys(Keys.SHIFT, Keys.INSERT)
    input_box.send_keys(Keys.ENTER)

    time.sleep(2)
