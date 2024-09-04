import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Edge()
driver.maximize_window()
url = "https://sahitest.com/demo/selectTest.htm"
driver.get(url)


sel01 = Select(driver.find_element(By.ID, 's1Id'))
sel02 = Select(driver.find_element(By.ID, 's2Id'))
sel03 = Select(driver.find_element(By.ID, 's3Id'))

# 使用索引选择下拉栏选项
sel01.select_by_index(2)  # o2
# 使用value选择下拉栏选项
sel02.select_by_value("o1")  # o1
# 使用可视值（.innerText）选择下拉栏选项
sel03.select_by_visible_text("o3")  # o3

time.sleep(3)
driver.close()