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
# 获取元素并点击
# find_element相当于js中的document.querySelector() 只选中第一个符合条件的元素
# driver.find_element(By.CLASS_NAME, 'channel-link').click()
# find_elements相当于js中的document.querySelectorAll() 选中所有符合条件的元素 返回一个列表
eleList = driver.find_elements(By.CLASS_NAME, 'channel-link')
for ele in eleList:
    print(ele.text)
# 等待3秒
time.sleep(3)
# 关闭浏览器
driver.close()
