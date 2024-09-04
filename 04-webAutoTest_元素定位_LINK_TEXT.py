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
# 选中text值为“番剧”的可跳转元素
# driver.find_element(By.LINK_TEXT, "番剧").click()
# 选中text值包含为“番剧”的可跳转元素（含href）
driver.find_element(By.PARTIAL_LINK_TEXT, "番剧").click()
# 等待3秒
time.sleep(3)
# 关闭浏览器
driver.quit()
