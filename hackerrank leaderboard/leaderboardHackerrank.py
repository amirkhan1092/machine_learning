from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

time.sleep(3)

##contest = 'b22-csea'  # add your contest name
'''b22-csea
b22-cseb
b22-csec
b22-csed
b22-csee
b22-csef
b22-cseg
b22-cseh
b22-csei
b22-csej
b22-csek
b22-csel
b22-csem
b22-cseop
b22-ecea
b22-eceb
b22-mca'''



lst = '''b22-csea
b22-cseb
b22-csec
b22-csed
b22-csee
b22-csef
b22-cseg
b22-cseh
b22-csei
b22-csej
b22-csek
b22-csel
b22-csem
b22-cseop
b22-ecea
b22-eceb
b22-mca'''.split()

obj = ChromeDriverManager().install()

for contest in lst:
    time.sleep(3)
    driver = webdriver.Chrome(obj)
    link = f"https://www.hackerrank.com/contests/{contest}/leaderboard"
    driver.get(link)
    time.sleep(3)
    ##driver.find_element_by_class_name('icon-cancel-small').click()

    try:
        el = driver.find_element_by_id('pagination-length')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == '100':
                option.click()
                time.sleep(8)

        leaderboardPage = driver.page_source

    except Exception as e:
        print('contest empty', e)
    else:
        soup = BeautifulSoup(leaderboardPage, 'html.parser')
        time.sleep(5)
        a_tags = soup.findAll("a", class_="cursor leaderboard-hackername rg_5")
        for a_tag in a_tags:
            with open(f'csv/all-{time.asctime()[:11]}.csv', 'a') as f:
                print(a_tag['data-value'], a_tag['data-attr10'], sep=',', file=f)

    driver.quit()

