from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
url = 'http://10.0.0.5/webauth.do?wlanacip=192.168.10.100&wlanacname=mzsf-bras&wlanuserip=10.19.57.87&mac=80:e1:bf:91' \
      ':e5:03&vlan=0&url=http://www.msftconnecttest.com '
driver.get(url)

"""
    键盘操作
        键盘操作封装在Keys类中
        操作：
            导包即可使用 Keys
        实例：
            driver.find_element(By.ID, 'passwd').send_keys(Keys.CONTROL, 'v')
        更多操作见Keys类
"""
userId = driver.find_element(By.ID, 'userId')
# 清空 userId
userId.clear()
# 输入 123456789001
userId.send_keys('123456789001')
sleep(2)
# 删除最后的 1
userId.send_keys(Keys.BACK_SPACE)
sleep(2)
# 全选 userId 里的内容
userId.send_keys(Keys.CONTROL, 'a')
# 复制
userId.send_keys(Keys.CONTROL, 'c')
sleep(2)
# 将内容粘贴到 passwd
driver.find_element(By.ID, 'passwd').send_keys(Keys.CONTROL, 'v')
sleep(2)

driver.quit()
