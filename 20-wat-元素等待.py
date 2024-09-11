"""
    元素等待：
        为什么需要元素等待？
            由于电脑配置或网络原因，在查找元素时，代码未在第一时间被加载出来，而抛出未找到元素异常
        什么是元素等待：
            元素在第一时间未找到时，元素等待的时长被激活，如果在设置时长内找到元素，继续执行代码，
            如果超出时长未找到元素，抛出未找到元素异常
        元素等待分类；
            隐式等待：
            显式等待：
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
# 每当查护照元素是，若一开始找不到元素，触发隐式等待
# 10s后若是还未找到元素则抛出未找到元素异常
driver.implicitly_wait(10)
url = 'https://www.bilibili.com/'
driver.get(url)

# 注：页面中没有id为123123的元素，会触发隐式等待 10s
driver.find_element(By.ID, '123123')
