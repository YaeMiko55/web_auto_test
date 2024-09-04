import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Edge()
driver.maximize_window()
url = "https://www.iviewui.com/view-ui-plus/component/form/cascader"
driver.get(url)

# 选中并点击下拉栏
driver.find_elements(By.XPATH, '//input[@class="ivu-input ivu-input-default"]')[0].click()
# 点击一个下拉栏选项
driver.find_element(By.XPATH, '//div[@class="ivu-cascader ivu-cascader-size-default ivu-cascader-visible"]//span[1]//ul[1]/li[2]').click()
# 点击一个下拉栏选项
driver.find_elements(By.XPATH, '//div[@class="ivu-cascader ivu-cascader-size-default ivu-cascader-visible"]//span//span//ul/li')[0].click()
# 点击一个下拉栏选项
driver.find_element(By.XPATH, '//div[@class="ivu-cascader ivu-cascader-size-default ivu-cascader-visible"]//span//span//span//ul/li').click()




time.sleep(3)
driver.close()