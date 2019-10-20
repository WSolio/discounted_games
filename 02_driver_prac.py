from selenium import webdriver
from time import sleep



driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")

url = "https://www.facebook.com/"

driver.get(url) #주소입력하고 ENTER 입력 기능

driver.find_element_by_id("email").send_keys("sonws1214@naver.com")
driver.find_element_by_id("pass").send_keys("a76081183!@s")
driver.find_element_by_id("u_0_4").click()


#sleep(5)


#pageString = driver.page_source
#print(pageString)

#인스타 껍데기만 크롤링
#인스타 내용 <div class = "Nnq7C xxx">


#driver.close()