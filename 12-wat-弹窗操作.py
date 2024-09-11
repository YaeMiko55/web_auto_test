import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# 1.只有确定的弹窗 alert
def alert_handle():
    # 打开浏览器
    driver = webdriver.Edge()
    driver.maximize_window()
    url = "https://sahitest.com/demo/alertTest.htm"
    driver.get(url)

    # 点击按钮弹出弹框
    driver.find_element(By.NAME, 'b1').click()
    # 使用switch_to.alert.text获取弹窗文字（.inner）
    print(driver.switch_to.alert.text)
    time.sleep(2)

    # 点击确定
    driver.switch_to.alert.accept()
    # 关闭浏览器
    time.sleep(3)
    driver.quit()


# 2.有确定和取消的弹窗 confirm
def confirm_handle():
    # 打开浏览器
    driver = webdriver.Edge()
    driver.maximize_window()
    url = "https://sahitest.com/demo/confirmTest.htm"
    driver.get(url)

    # 点击按钮弹出弹框
    driver.find_element(By.NAME, 'b1').click()
    time.sleep(2)

    # 点击确定
    driver.switch_to.alert.accept()
    time.sleep(2)
    # 点击取消
    # driver.switch_to.alert.accept()
    # time.sleep(2)

    # 关闭浏览器
    driver.quit()


# 3.有输入框的弹窗 prompt
def prompt_handle():
    # 打开浏览器
    driver = webdriver.Edge()
    driver.maximize_window()
    url = "https://sahitest.com/demo/promptTest.htm"
    driver.get(url)
    # 点击按钮弹出弹框
    driver.find_element(By.NAME, 'b1').click()
    time.sleep(2)
    # 输入内容
    prompt = driver.switch_to.alert
    prompt.send_keys('prompt123')
    prompt.accept()
    time.sleep(2)


if __name__ == '__main__':
    # 1.只有确定的弹窗 alert
    # alert_handle()
    # 2.有确定和取消的弹窗 confirm
    # confirm_handle()
    # 3.有输入框的弹窗 prompt
    prompt_handle()
    pass
