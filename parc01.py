from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

from bs4 import BeautifulSoup

usr = 'sonws1214@naver.com'
pwd = 'a76081183!@s'

path = "C:/chromedriver"
driver = webdriver.Chrome(path)
driver.get("http://www.facebook.org")

assert "Facebook" in driver.title

elem = driver.find_element_by_id("email")
elem.send_keys(usr)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

driver.implicitly_wait(5)
driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)

driver.implicitly_wait(5)
driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)

for i in range(5):
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    driver.implicitly_wait(3)
    time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

posts = soup.select('div.text_exposed_root')

for post in posts:
    print(post.text)