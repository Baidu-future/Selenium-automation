import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    def test_1(self):
        driver=webdriver.Firefox()
        driver.get('http://localhost/upload/index.php')#首页
        driver.find_element(By.ID,'keyword').send_keys('806')#关键字
        driver.find_element(By.NAME,'imageField').click()
        sleep(4)
        driver.quit()

    def test_2(self):
        driver=webdriver.Firefox()
        driver.get('http://localhost/upload/index.php')#首页
        driver.find_element(By.ID,'keyword').send_keys('abcde')#关键字
        driver.find_element(By.NAME,'imageField').click()
        sleep(4)
        driver.quit()

    def test_3(self):
        driver=webdriver.Firefox()
        driver.get('http://localhost/upload/index.php')#首页
        driver.find_element(By.NAME,'imageField').click()
        sleep(4)
        driver.quit()

if __name__ == '__main__':
    unittest.main()
