from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
import keyboard
import time
# driver = webdriver.Chrome()

driver.get('http://172.16.10.20:1000/login?')
tmp = driver.find_element_by_id('ft_un')
tmp.click()
tmp.send_keys('amir.khan')
time.sleep(2)
tmp2 = driver.find_element_by_id('ft_pd')
tmp2.click()
tmp2.send_keys('54892044')
time.sleep(2)
tmp3 = driver.find_element_by_xpath('/html/body/div/div/form/div[3]/input')
tmp3.click()
# password = driver.find_element_by_id('dl_role')
# password.send_keys('amir@gla')

# psd = driver.find_element_by_class_name('row login-form')
# psd.send_keys('amir@gla')



# password = driver.find_element_by_id('txt_password')
# password.send_keys('amir@gla')



# password = driver.find_element_by_xpath('//*[@id="ft_pd"]')
# password.send_keys('54892044')
#
# button = driver.find_element_by_xpath('/html/body/div/div/form/div[3]/input')
# button.click()



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