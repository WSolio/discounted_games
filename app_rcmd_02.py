import requests
from bs4 import BeautifulSoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://play.google.com/store/apps/collection/cluster?clp=ChwKGgoUdG9wc2VsbGluZ19wYWlkX0dBTUUQBxgD:S:ANO1ljI3NIA&gsr=Ch4KHAoaChR0b3BzZWxsaW5nX3BhaWRfR0FNRRAHGAM%3D:S:ANO1ljKgPH8',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')


games=soup.select('#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > div')

print(games)



#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > div:nth-child(1) > c-wiz > div > div > div.RZEgze > div > div > div.bQVA0c > div > div > div.b8cIId.ReQCgd.Q9MA7b > a > div

#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > c-wiz:nth-child(200) > div > div > div.RZEgze > div > div > div.bQVA0c > div > div > div.b8cIId.ReQCgd.Q9MA7b > a > div