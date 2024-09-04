import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
url = "https://sahitest.com/demo/iframesTest.htm"
driver.get(url)

# 外层html
driver.find_element(By.ID, 'checkRecord').clear()
time.sleep(1)
driver.find_element(By.ID, 'checkRecord').send_keys("hello world")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'input[type="button"]').click()

# 进入iframe框架内部 使用索引定位
driver.switch_to.frame(0)
driver.find_element(By.XPATH, '//a[@href="linkTest.htm"]').click()
time.sleep(3)
driver.close()

# 进入iframe框架内部 使用id定位 使用name定位
driver = webdriver.Edge()
driver.maximize_window()
url = "file:///D:/python_prj/pythonProject/html_test/iframe_test.html"
driver.get(url)

# 通过id进入iframe框架内部
driver.switch_to.frame("baidu")
# 点击新闻
driver.find_element(By.XPATH, '//a[text()="新闻"]').click()
time.sleep(3)
driver.quit()

# 通过元素进入iframe框架内部
driver = webdriver.Edge()
driver.maximize_window()
url = "https://sahitest.com/demo/iframesTest.htm"
driver.get(url)

ele = driver.find_element(By.CSS_SELECTOR, 'body > iframe')
driver.switch_to.frame(ele)

driver.find_element(By.XPATH, '//a[@href="linkTest.htm"]').click()

# 返回上一层html
driver.switch_to.parent_frame()
driver.find_element(By.ID, 'checkRecord').clear()
time.sleep(1)
driver.find_element(By.ID, 'checkRecord').send_keys("回到了外层html")
time.sleep(1)

# 返回最外层html
driver.switch_to.default_content()

driver.close()
