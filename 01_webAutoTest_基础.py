import time

from selenium import webdriver

from selenium.webdriver.common.by import By

# 创建一个Edge浏览器对象
driver = webdriver.Edge()
# 打开网页
url = "https://www.bilibili.com"
driver.get(url)
# 在搜索框中输入内容
driver.find_element(By.CLASS_NAME, 'nav-search-input').send_keys("python")
# 点击搜索按钮
driver.find_element(By.CLASS_NAME, 'nav-search-btn').click()
time.sleep(3)
# 关闭浏览器
driver.close()
