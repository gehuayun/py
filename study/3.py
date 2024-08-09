import autopep8 as autopep8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


def gj_ss():
    dr_1 = webdriver.Chrome()
    dr_1.get('http://www.baidu.com')
    dr_1.maximize_window()
    dr_1.implicitly_wait(20)
    al = dr_1.find_element(By.ID, "s-usersetting-top")
    ActionChains(dr_1).move_to_element(al).perform()
    time.sleep(3)
    dr_1.find_element(By.XPATH, '//*[@id="s-user-setting-menu"]/div/a[2]/span').click()
    dr_1.find_element(By.ID, 'adv_keyword').send_keys('XPATH')
    time.sleep(1)
    dr_1.find_element(By.XPATH, '//*[@id="adv-setting-8"]/input[2]').click()
    time.sleep(5)

# gj_ss()

dr_2 =webdriver.Chrome()
dr_2.get('http://blog.csdn.net')
dr_2.maximize_window()
dr_2.implicitly_wait(20)
# dr_2.find_element(By.XPATH, '//*[@id="passportbox"]/img').click()
# dr_2.find_element(By.XPATH, '//*[@id="toolbar-search-input"]').send_keys('welcome')
# time.sleep(3)
# dr_2.find_element(By.XPATH, '//*[@id="toolbar-search-button"]/span').click()
# time.sleep(3)
d2 = dr_2.find_element(By.XPATH, '//*[@id="floor-blog-nav_746"]/div/div/img')
ActionChains(dr_2).move_to_element(d2).perform()
time.sleep(3)
dr_2.find_element(By.XPATH, '//*[@id="floor-blog-nav_746"]/div/div/div/ul/li[9]/a').click()
time.sleep(3)
dr_2.find_element(By.XPATH, '//*[@id="floor-blog-nav_746"]/div/div/div/ul/li[25]/a').click()
time.sleep(3)
dr_2.find_element(By.XPATH, '//*[@id="floor-blog-nav_746"]/div/div/div/ul/li[29]/a').click()
time.sleep(3)
dr_2.find_element(By.XPATH, '//*[@id="floor-blog-nav_746"]/div/div/div/ul/li[41]/a').click()
time.sleep(3)


