import time

from selenium import webdriver

from selenium.webdriver.common.by import By

# 创建一个Edge浏览器对象
driver = webdriver.Edge()
# 打开网页
url = "https://www.baidu.com"
driver.get(url)
# 最大化
driver.maximize_window()
# 在搜索框中输入内容
driver.find_element(By.ID, 'kw').send_keys('selenium')
# 点击搜索按钮
driver.find_element(By.ID, 'su').click()
time.sleep(3)
# 关闭浏览器
driver.close()
