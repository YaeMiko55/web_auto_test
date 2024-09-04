import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
url = "https://www.iviewui.com/view-ui-plus/component/form/checkbox"
driver.get(url)

# 选中移动端系统单选框
checkboxs = driver.find_elements(By.XPATH, '//div[@data-title="组合使用"]//input[@type="checkbox"]')

for i in range(4):
  checkboxs[i].click()
  time.sleep(2)

driver.close()
