import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def setup(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    return driver


def teardown(driver):
    driver.quit()


def test_sellShop():
    # 打开网页
    driver = setup('http://sellshop.5istudy.online/sell/user/login_page')
    # 输入账号
    driver.find_element(By.ID, 'username').send_keys('test13')
    # 输入密码
    driver.find_element(By.ID, 'password').send_keys('123456')
    # 点击登录
    driver.find_element(By.CSS_SELECTOR, 'input[value="登录"]').click()

    # 点击新增
    driver.find_element(By.LINK_TEXT, '新增').click()
    # 输入名称
    driver.find_element(By.NAME, 'productName').send_keys('新鲜邦布')
    # 输入价格
    driver.find_element(By.NAME, 'productPrice').send_keys('90')
    # 输入库存
    driver.find_element(By.NAME, 'productStock').send_keys('1')
    # 输入描述
    driver.find_element(By.NAME, 'productDescription').send_keys('刚出炉的邦布')
    # 输入图片地址
    driver.find_element(By.NAME, 'productIcon').send_keys('https://tse3-mm.cn.bing.net/th/id/OIP-C.0AvgH-9GQ7dX5zfrI-kvvAAAAA?rs=1&pid=ImgDetMain')
    # 选择类目
    Select(driver.find_element(By.NAME, 'categoryType')).select_by_visible_text("零食饮料")
    # 点击提交
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    teardown(driver)


if __name__ == '__main__':
    test_sellShop()

