import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


"""
    常用浏览器操作api：
    
        最大化窗口：driver.maximize_window()
        设置浏览器窗口大小：driver.set_window_size(400, 300)
        设置浏览器窗口位置：driver.set_window_position(200, 100)
        
        回退：driver.back()
        前进：driver.forward()
        刷新：driver.refresh()
        
        获取页面title：driver.title
        获取当前界面url：driver.current_url
                
"""

driver = webdriver.Edge()
url = 'https://search.cctv.com/search.php'
driver.get(url)

# 设置浏览器窗口大小
driver.set_window_size(400, 300)
sleep(3)

# 设置浏览器窗口位置
driver.set_window_position(200, 100)
sleep(3)

# 最大化浏览器窗口
driver.maximize_window()
sleep(3)

# 关闭浏览器
driver.close()

driver = webdriver.Edge()
url = 'https://search.cctv.com/search.php'
driver.maximize_window()
driver.get(url)

driver.find_element(By.ID, 'search_qtext').send_keys('台风')
driver.find_element(By.XPATH, '//a[@onclick="searchForm_submit();"]').click()
sleep(3)
driver.find_element(By.ID, 'search_qtext').clear()
driver.find_element(By.ID, 'search_qtext').send_keys('摩羯')
driver.find_element(By.XPATH, '//a[@onclick="searchForm_submit();"]').click()
sleep(3)

# 获取页面title
print(driver.title)
# 获取当前界面url

print(driver.current_url)

# 回退
driver.back()
sleep(3)

# 前进
driver.forward()
sleep(3)

driver.find_element(By.ID, 'search_qtext').send_keys('登陆')
sleep(3)

# 刷新
driver.refresh()
sleep(3)

driver.quit()
