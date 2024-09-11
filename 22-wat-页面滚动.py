from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
url = "https://www.bilibili.com"
driver.get(url)

# 方法1 使用 PagDown PagUp 实现
driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_UP)
sleep(1)

# 方法2 通过 js 操作 windows
js = 'window.scrollTo(0, 1000)'
driver.execute_script(js)
sleep(2)

sleep(2)
driver.quit()
