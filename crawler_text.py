from selenium import webdriver
from bs4 import BeautifulSoup

import time

driver = webdriver.Chrome('C:/chromedriver')
driver.get('https://play.google.com/store/apps/collection/cluster?clp=ChwKGgoUdG9wc2VsbGluZ19wYWlkX0dBTUUQBxgD:S:ANO1ljI3NIA&gsr=Ch4KHAoaChR0b3BzZWxsaW5nX3BhaWRfR0FNRRAHGAM%3D:S:ANO1ljKgPH8&gsr=Ch4KHAoaChR0b3BzZWxsaW5nX3BhaWRfR0FNRRAHGAM%3D:S:ANO1ljKgPH8')

for i in range(4):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)

game_detail = driver.find_elements_by_class_name('Vpfmgd')
top_game_details = driver.find_elements_by_class_name('bQVA0c')
price_list = driver.find_elements_by_class_name('zYPPle')
discounted_price_list = driver.find_elements_by_class_name('SUZt4c djCuy')

games = []

for game in game_detail:
    a=game.text
    b=game.src
    games.append(a)
    if '0₩' in a:
        print(num, a)


#for price in discounted_price_list:
#    b = price.text
#    print(b)
#    num = num+1

driver.quit()