import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

url = 'https://www.olx.co.id/items/q-handphone'
path = 'C:\webdrivers\chromedriver.exe'

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-infobar')
chrome_options.add_argument('disable-notifications')

driver = webdriver.Chrome(executable_path=path, options=chrome_options)
driver.get(url)
datas = []

html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(html, 'html.parser')
items = soup.findAll('li', 'EIR5N')
# print(soup.findAll)
for i in items :
    name = i.find('span', '_2tW1I').text
    print(name)
    price = i.find('span', '_89yzn').text
    location = i.find('span', 'tjgMj').text
    date = i.find('span', 'zLvFQ').text
    datas.append([name,price,location,date])

# for i in datas:
#     print(i)

driver.close()

headers_exel = ['name', 'price', 'location', 'date']
writer = csv.writer(open('result/data_tokped.csv', 'w', newline=''))

writer.writerow(headers_exel)
for i in datas:
    writer.writerow(i)