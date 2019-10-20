import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import time

#driver = webdriver.Chrome('C:/chromedriver')
#driver.get('https://play.google.com/store/apps/collection/cluster?clp=ChwKGgoUdG9wc2VsbGluZ19wYWlkX0dBTUUQBxgD:S:ANO1ljI3NIA&gsr=Ch4KHAoaChR0b3BzZWxsaW5nX3BhaWRfR0FNRRAHGAM%3D:S:ANO1ljKgPH8&gsr=Ch4KHAoaChR0b3BzZWxsaW5nX3BhaWRfR0FNRRAHGAM%3D:S:ANO1ljKgPH8')

#for i in range(5):
#    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#    time.sleep(3)




#셀레니움 뷰티풀숲 예제 driver.~~~


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://play.google.com/store/apps/collection/cluster?clp=ChwKGgoUdG9wc2VsbGluZ19wYWlkX0dBTUUQBxgD:S:ANO1ljI3NIA&gsr=Ch4KHAoaChR0b3BzZWxsaW5nX3BhaWRfR0FNRRAHGAM%3D:S:ANO1ljKgPH8',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')


games =soup.select('#fcxH9b > div.WpDbMd > c-wiz > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > div')
games_02 =soup.select('#fcxH9b > div.WpDbMd > c-wiz > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > c-wiz')


# c-wiz > div > div > div.RZEgze > div > div > div.Z2nl8b > div > div.zYPPle > div > button > div > span > span
# c-wiz > div > div > div.RZEgze > div > div > div.Z2nl8b > div > div.zYPPle > div > button > div > span.SUZt4c.djCuy > span
# c-wiz > div > div > div.RZEgze > div > div > div.Z2nl8b > div > div.zYPPle > div > button > div > span.VfPpfd.ZdBevf.i5DZme




for game in games:
    a = game.select_one('c-wiz > div > div > div.RZEgze > div > div > div.bQVA0c > div > div > div.b8cIId.ReQCgd.Q9MA7b > a > div')
    if not a == None:
        title = a.text
        publisher = game.select_one('c-wiz > div > div > div.RZEgze > div > div > div.bQVA0c > div > div > div.b8cIId.ReQCgd.KoLSrc > a > div').text
        price = game.select_one('c-wiz > div > div > div.RZEgze > div > div > div.Z2nl8b > div > div.zYPPle > div > button > div > span > span')
        discounted_price = game.select_one('c-wiz > div > div > div.RZEgze > div > div > div.Z2nl8b > div > div.zYPPle > div > button > div > span.VfPpfd.ZdBevf.i5DZme')
        if not discounted_price.text == price.text:
            print(title, '\n     published by', publisher, '\n       ' ,price.text,'에서' ,discounted_price.text, '으로 할인중!')


for


#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > c-wiz:nth-child(200) > div > div > div.RZEgze > div > div > div.bQVA0c > div > div > div.b8cIId.ReQCgd.Q9MA7b > a > div