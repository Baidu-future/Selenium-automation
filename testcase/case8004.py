import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from ddt import ddt,data,unpack
from utils.read_csv import CSVUtil

# 读取csv文件里的测试数据
u=CSVUtil('..\\testdata\\data2.csv')
d=u.get_list_data()
print(d)

@ddt
class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(12)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    @data(*d)
    @unpack
    def test_something(self,user,pwd):
        print(user,pwd)
        self.driver.get('http://localhost/upload/user.php')#打开前台登录页
        self.driver.find_element(By.NAME,'username').send_keys(user)#用户名
        self.driver.find_element(By.NAME,'password').send_keys(pwd)#密码
        self.driver.find_element(By.NAME,'submit').click()#立即登陆
        sleep(1)
        # 检查网页源代码里包含“用户名或密码错误”
        ps1=self.driver.page_source
        self.assertIn('用户名或密码错误',ps1)


if __name__ == '__main__':
    unittest.main()
