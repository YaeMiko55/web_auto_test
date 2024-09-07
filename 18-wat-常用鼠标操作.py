from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

"""
    常用鼠标操作
        左键单击
        左键双击
        右键单击
        悬停
"""

driver = webdriver.Edge()
driver.maximize_window()
url = 'https://swiper.com.cn/'
driver.get(url)

# 实例化ActionChains类
action = ActionChains(driver)

# 获取搜索框
search = driver.find_element(By.ID, 'search-keyword')
# 输入”滚动“
search.send_keys("滚动")
sleep(2)

# 双击搜索框选中”滚动“
action.double_click(search).perform()
sleep(2)

# 输入”3D“
search.send_keys("3D")
sleep(2)

# 获取”在线演示“
online = driver.find_element(By.CSS_SELECTOR, '#nav > li:nth-child(3)')

# 将鼠标悬停在”在线演示上“
action.move_to_element(online).perform()
sleep(2)

# 获取子集选项
onlineChr = driver.find_element(By.CSS_SELECTOR, '#nav > li:nth-child(3) > ul > li:nth-child(1) > a')

# 左键单击子集选项
action.click(onlineChr).perform()
# action.context_click(onlineChr).perform()  # context_click为右击
sleep(2)

# 点击基础滑动
driver.find_element(By.CSS_SELECTOR, 'li.default').click()
sleep(1)

# 回退
driver.back()

# 拖拽
# action.drag_and_drop('目标元素', '托到哪个元素上').perform()
# action.move_by_offset(xoffset=100, yoffset=200).perform()  # 拖动距离

driver.quit()
