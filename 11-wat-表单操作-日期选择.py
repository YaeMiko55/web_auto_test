import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
driver.maximize_window()
url = "https://www.iviewui.com/view-ui-plus/component/form/date-picker"
driver.get(url)

# 时间点
driver.find_elements(By.XPATH, '//input[@class="ivu-input ivu-input-default ivu-input-with-suffix"]')[0].send_keys("2024-9-9")

# 时间段
driver.find_elements(By.XPATH, '//input[@class="ivu-input ivu-input-default ivu-input-with-suffix"]')[1].send_keys("2024-9-9 - 2024-9-20")

time.sleep(3)
driver.close()
