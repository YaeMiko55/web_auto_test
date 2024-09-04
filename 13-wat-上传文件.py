import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.get_file_path import get_file_path

driver = webdriver.Edge()
driver.maximize_window()
url = "https://sahitest.com/demo/php/fileUpload.htm"
driver.get(url)

# 点击上传文件按钮
uploadPath = driver.find_element(By.ID, "file")

# 补充 python 的文件操作 详情见 utils/get_file_path.py
img_path = get_file_path("1.png")
# print(path)

# 上传文件的路径
uploadPath.send_keys(img_path)
# 点击提交按钮
driver.find_element(By.NAME, "submit").click()



time.sleep(3)
driver.close()
