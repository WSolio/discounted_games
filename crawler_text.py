from selenium import webdriver
from bs4 import BeautifulSoup

import time

driver = webdriver.Chrome('C:/chromedriver')
driver.get('https://play.google.com/store/apps/collection/cluster?clp=ChwKGgoUdG9wc2VsbGluZ19wYWlkX0dBTUUQBxgD:S:ANO1ljI3NIA&gsr=Ch4KHAoaChR0b3BzZWxsaW5nX3BhaWRfR0FNRRAHGAM%3D:S:ANO1ljKgPH8&gsr=Ch4KHAoaChR0b3BzZWxsaW5nX3BhaWRfR0FNRRAHGAM%3D:S:ANO1ljKgPH8')

for i in range(4):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)

game_titles = driver.find_elements_by_class_name('WsMG1c') ###게임 제목
game_publishers = driver.find_elements_by_class_name('KoLSrc') ###게임 제작사
game_origin_prices = driver.find_elements_by_class_name('SUZt4c') ###게임 원래 가격 <---이 값이 존재하는 게임은 할인중인 게임
game_saling_prices = driver.find_elements_by_class_name('VfPpfd') ###게임 세일 가격 <---할인되거나, 일반적인 가격
game_prices = driver.find_elements_by_class_name('LCATme') ###게임 종합 가격 <---둘 다 포함되는 영역


#T75of QNCnCf
#fcxH9b > div.WpDbMd > c-wiz > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > div:nth-child(1) > c-wiz > div > div > div.uzcko > div > span.yNWQ8e.K3IMke.buPxGf > span > img
game_detail = driver.find_elements_by_class_name('VfPpfd')

print(game_detail)

games = []


#우선 origin price가 존재하는 영역의 제목, 제작사, 판매가격을 리스트에 넣어야 하는데.
#그 방법을 모르겠음....
num = 1
for game_price in game_prices:
    a = game_price.text
for game_origin_price in game_origin_prices:
    b = game_origin_price.text
for game_saling_price in game_saling_prices:
    c = game_saling_price.text

if a == b + c:
    games.append(b)
    games.append(c)
    print(games)


#for game_title in game_titles:
#    title = game_title.text
#    games.append(title)

################### 제작사 한개만 리스팅 ####################
#for game_publisher in game_publishers:
#    publisher = game_publisher.text
#    if num % 2 == 1:
#        games.append(publisher)
#        print(round(num * 0.5), a)
#    num = num + 1





driver.quit()