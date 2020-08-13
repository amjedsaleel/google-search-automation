from selenium import webdriver
from config import USERNAME, PASSWORD
import time

users = ['amjed_saleel', 'jasim_ak', 'haseeb_rz', '______adharsh_us_______']

browser = webdriver.Chrome(executable_path='/home/amjed/chromedriver/chromedriver')
browser.maximize_window()
browser.get('https://instagram.com')

time.sleep(2)

username =  browser.find_element_by_name('username')
username.send_keys(USERNAME)

password = browser.find_element_by_name('password')
password.send_keys(PASSWORD)

time.sleep(1)

login_btn = browser.find_element_by_css_selector('button[type="submit"]')
login_btn.click()

time.sleep(2)

for user in users:
    browser.get(f"https://www.instagram.com/{user}/")
    posts, followers, following = browser.find_elements_by_class_name('g47SY')
    print(posts.text, followers.text, following.text)

    bio = browser.find_element_by_class_name('-vDIg')
    print(bio.text)

    with open(f'{user}.txt', 'w') as file:
        file.write(f"Number of posts: {posts.text}\nFollowers: {followers}.text\nFollowing: {following.text}\n\nBio: {bio.text}")

    time.sleep(1)

