from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

# driver = webdriver.Chrome()

driver.get('172.16.10.20:1000/login?')

user_name = driver.find_element_by_xpath('//*[@id="ft_un"]')
user_name.send_keys('amir.khan')

password = driver.find_element_by_xpath('//*[@id="ft_pd"]')
password.send_keys('54892044')

button = driver.find_element_by_xpath('/html/body/div/div/form/div[3]/input')
button.click()



# from webdriver_manager.chrome import ChromeDriverManager
# import time
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
# link = "172.16.10.20:1000/login?"
# driver.get(link)
#
# ##driver.find_element_by_class_name('icon-cancel-small').click()
# page_source = driver.page_source
#
# el = driver.find_element_by_id('pagination-length')
# for option in el.find_elements_by_tag_name('option'):
#         if option.text == '100':
#             option.click()
#             time.sleep(8)
#
# leaderboardPage = driver.page_source