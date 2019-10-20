import requests
from bs4 import BeautifulSoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://play.google.com/store/apps/collection/cluster?clp=ChwKGgoUdG9wc2VsbGluZ19wYWlkX0dBTUUQBxgD:S:ANO1ljI3NIA&gsr=Ch4KHAoaChR0b3BzZWxsaW5nX3BhaWRfR0FNRRAHGAM%3D:S:ANO1ljKgPH8',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > c-wiz:nth-child(67) > div > div > div.RZEgze > div > div > div.bQVA0c > div > div > div.b8cIId.ReQCgd.Q9MA7b > a > div

#스크롤 전
#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > div:nth-child(50)
#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > div:nth-child(50) > c-wiz > div > div > div.RZEgze > div > div > div.bQVA0c > div > div > div.b8cIId.ReQCgd.Q9MA7b > a > div


#스크롤 후
#fcxH9b > div.WpDbMd > c-wiz:nth-child(5)

#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > c-wiz:nth-child(51)
#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > c-wiz:nth-child(51) > div
#제목
#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > c-wiz:nth-child(136) > div > div > div.RZEgze > div > div > div.bQVA0c > div > div > div.b8cIId.ReQCgd.Q9MA7b > a > div
#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > c-wiz:nth-child(51) > div > div > div.RZEgze > div > div > div.bQVA0c > div > div > div.b8cIId.ReQCgd.Q9MA7b > a > div
#제조사
#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > c-wiz:nth-child(51) > div > div > div.RZEgze > div > div > div.bQVA0c > div > div > div.b8cIId.ReQCgd.KoLSrc > a > div
#가격
#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > c-wiz:nth-child(53) > div > div > div.RZEgze > div > div > div.Z2nl8b > div > div.zYPPle > div > button > div > span.VfPpfd.ZdBevf.i5DZme > span
#할인가
#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > c-wiz:nth-child(53) > div > div > div.RZEgze > div > div > div.Z2nl8b > div > div.zYPPle > div > button > div > span.SUZt4c.djCuy > span


games =soup.select('#fcxH9b > div.WpDbMd > c-wiz > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd> c-wiz > div >  div')


for game in games:
    a = game.select_one(' div.RZEgze > div > div > div.bQVA0c > div > div > div.b8cIId.ReQCgd.Q9MA7b > a > div')
    print(a.text)

# > div > div > div.RZEgze > div > div > div.bQVA0c > div > div > div.b8cIId.ReQCgd.Q9MA7b > a > div

#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > c-wiz:nth-child(136) > div > div > div.RZEgze > div > div > div.bQVA0c > div > div > div.b8cIId.ReQCgd.Q9MA7b > a > div