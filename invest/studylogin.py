from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def 登录学习平台():
    dr = webdriver.Firefox()

    dr.get("https://smzdm.yunxuetang.cn/login.htm")
    WebDriverWait(dr, 20, 0.5).until(EC.presence_of_element_located((By.ID,"qrPwdLogin")))
    dr.find_element_by_xpath('//*[@id="qrPwdLogin"]').click()
    time.sleep(2)
    dr.find_element_by_xpath('//*[@id="txtUserName2"]').send_keys("chencheng01")
    dr.find_element_by_xpath('//*[@id="txtPassword2"]').send_keys("123456")
    dr.find_element_by_xpath('//*[@id="btnLogin2"]').click()
    time.sleep(3)
    return ("陈程01" in dr.page_source)



if __name__ == '__main__':
    登录学习平台()
