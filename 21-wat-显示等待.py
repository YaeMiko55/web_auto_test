from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
driver.maximize_window()
url = 'https://www.bilibili.com/'
driver.get(url)

"""
    显式等待：
        方法封装在WebDriverWait包中
        WebDriverWait(driver, 等待时间, 搜索时间间隔 默认0.5).until(要寻找的元素)
        返回要找的元素
    示例：
"""

WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element(By.ID, '123123'))
# 匿名函数中 x 为 driver 
