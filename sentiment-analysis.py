from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv

options = Options()
options.chrome_executable_path = "/chromedriver.exe"
driver = webdriver.Chrome(options=options)
driver.get('https://www.ptt.cc/bbs/Gossiping/index.html')
button = driver.find_element(By.NAME, "yes")
button.click()
soup = BeautifulSoup(driver.page_source, 'lxml')
title = soup.find_all('div', class_='title')
urls = []
for t in title:
    text = t.find('a').text
    if text and '[公告]' not in text:
        url = t.find('a').get('href')
        if url:
            urls.append(url)

with open('sentiment-analysis.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['text', 'label'])

    for u in urls:
        driver.get('https://www.ptt.cc' + u)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        content = soup.find('div', id='main-content')
        tag = content.find_all('div')
        for s in tag:
            s.decompose()
        span = content.find_all('span')
        for s in span:
            s.decompose()
        str = content.text.split()
        for s in str:
            s = s.split('，')
            for i in s:
                if i != '--' and i != '':
                    writer.writerow([i, ''])

driver.close()
