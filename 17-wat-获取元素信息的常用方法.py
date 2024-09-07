from selenium import webdriver
from selenium.webdriver.common.by import By

"""
    # 获取元素文本             ele.text
    # 获取元素大小像素          ele.size
                
    # 获取元素属性值            ele.get_attribute("href")
    # 判断元素是否可见          ele.is_displayed()
    # 判断元素是否可用          ele.is_enabled()
    # 判断元素是否被选中        ele.is_selected()
"""

driver = webdriver.Edge()
driver.maximize_window()
url = 'https://login.sina.com.cn/signup/signup'
driver.get(url)

# 获取元素文本
agreeText = driver.find_elements(By.CSS_SELECTOR, 'p.agreement>a')[0].text
print('元素中的文本：', agreeText)
# 获取元素大小（像素）
agreeSize = driver.find_elements(By.CSS_SELECTOR, 'p.agreement>a')[0].size
print('元素中的大小：', agreeSize)
# 获取元素属性值
agreeAttribute = driver.find_elements(By.CSS_SELECTOR, 'p.agreement>a')[0].get_attribute("href")
print('元素的“href属性值“：', agreeAttribute)
# 判断元素是否可见
agreeDisplayed = driver.find_elements(By.CSS_SELECTOR, 'p.agreement>a')[0].is_displayed()
print('元素是否可见：', agreeDisplayed)
# 判断元素是否可用
agreeEnabled = driver.find_elements(By.CSS_SELECTOR, 'p.agreement>a')[0].is_enabled()
print('元素是否可用：', agreeEnabled)
# 判断元素是否被选中
driver.find_element(By.CSS_SELECTOR, 'input[value="23"]').click()
isSelected_01 = driver.find_element(By.CSS_SELECTOR, 'input[value="23"]').is_selected()
isSelected_02 = driver.find_element(By.CSS_SELECTOR, 'input[value="18"]').is_selected()
print(isSelected_01, isSelected_02)

driver.quit()
