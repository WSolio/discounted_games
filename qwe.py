from bs4 import BeautifulSoup
from pprint import pprint
import requests



html = requests.get("https://play.google.com/store/apps/collection/cluster?clp=ChwKGgoUdG9wc2VsbGluZ19wYWlkX0dBTUUQBxgD:S:ANO1ljI3NIA&gsr=Ch4KHAoaChR0b3BzZWxsaW5nX3BhaWRfR0FNRRAHGAM%3D:S:ANO1ljKgPH8&gsr=Ch4KHAoaChR0b3BzZWxsaW5nX3BhaWRfR0FNRRAHGAM%3D:S:ANO1ljKgPH8")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

data1=soup.findAll('div', {'class' : 'RZEgze'})

for title in data1:
    print(title.get_text())