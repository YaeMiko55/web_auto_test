import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
url = "https://www.iviewui.com/view-ui-plus/component/form/radio"
driver.get(url)

# 选中移动端系统单选框
radios = driver.find_elements(By.XPATH, '//input[@type="radio" and @class="ivu-radio-input"]')

for i in range(1,4):
  radios[i].click()
  time.sleep(2)

driver.close()
