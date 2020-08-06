from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
time.sleep(3)
driver = webdriver.Chrome(ChromeDriverManager().install())
contest = 'python38-12'
link = f"https://www.hackerrank.com/contests/{contest}/leaderboard"
driver.get(link)

##driver.find_element_by_class_name('icon-cancel-small').click()
page_source = driver.page_source

el = driver.find_element_by_id('pagination-length')
for option in el.find_elements_by_tag_name('option'):
    if option.text == '100':
        option.click()
        time.sleep(8)

leaderboardPage = driver.page_source
driver.quit()
leaderboardPage
time.sleep(10)

soup = BeautifulSoup(leaderboardPage, 'html.parser')
time.sleep(5)
a_tags = soup.findAll("a", class_="cursor leaderboard-hackername rg_5")
for a_tag in a_tags:
    with open('scoreSecB.csv', 'a') as f:
        print(a_tag['data-value'], a_tag['data-attr10'], sep=',', file=f)

