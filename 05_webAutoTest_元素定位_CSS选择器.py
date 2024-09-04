import time

from selenium import webdriver

from selenium.webdriver.common.by import By

# 创建一个Edge浏览器对象
driver = webdriver.Edge()
# 打开网页
url = "https://www.bilibili.com"
driver.get(url)
# 最大化
driver.maximize_window()

# 通过CSS选择器定位元素
eleList = driver.find_elements(By.CSS_SELECTOR, ".carousel-inner__img>img")
for ele in eleList:
    print(ele.get_attribute("alt"), "\n", ele.get_attribute("src"))
