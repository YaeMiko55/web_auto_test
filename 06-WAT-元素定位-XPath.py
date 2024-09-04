import time

from selenium import webdriver

from selenium.webdriver.common.by import By

# 创建一个Edge浏览器对象
driver = webdriver.Edge()
# 最大化
driver.maximize_window()
# 打开网页
url = "https://www.baidu.com"
driver.get(url)

# 通过XPath定位新闻 可以使用and实现多个条件定位元素
eleList = driver.find_elements(By.XPATH, '//a[@class="mnav c-font-normal c-color-t" and @target="_blank"]')
for ele in eleList:
    ele.click()
# 停留10秒
time.sleep(10)
# 关闭浏览器
driver.quit()
