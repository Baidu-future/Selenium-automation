import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    # setUp：业务无关的准备工作的步骤
    def setUp(self):
        self.driver=webdriver.Firefox()#启动浏览器
        self.driver.implicitly_wait(13)#隐式等待
        self.driver.maximize_window()#最大化浏览器

    def tearDown(self):
        self.driver.quit()

    def test_1(self):
        self.driver.get('http://localhost/upload/user.php')
        self.driver.find_element(By.NAME,'username').send_keys('vip')#用户名
        self.driver.find_element(By.NAME,'password').send_keys('vip')#密码
        self.driver.find_element(By.NAME,'submit').click()#立即登录
        sleep(1)
        # 获得当时的网页源代码---注意：该步骤前面不要等待超过3秒
        ps1=self.driver.page_source
        # 检查其中包含“登录成功” ---注意：录
        self.assertIn('登录成功',ps1)
        # 检查界面上方红色的用户名是vip    <font class="f4_b">vip</font>
        t1=self.driver.find_element(By.XPATH,'//font[@id="ECS_MEMBERZONE"]/font/font').text
        self.assertEqual('vip',t1)


    def test_2(self):
        self.driver.get('http://localhost/upload/user.php')
        self.driver.find_element(By.NAME,'username').send_keys('111')#用户名
        self.driver.find_element(By.NAME,'password').send_keys('222')#密码
        self.driver.find_element(By.NAME,'submit').click()#立即登录
        sleep(1)
        # 练习：检查网页源代码里包含“用户名或密码错误”
        ps2=self.driver.page_source
        self.assertIn('用户名或密码错误',ps2)


    def test_3(self):
        self.driver.get('http://localhost/upload/user.php')
        self.driver.find_element(By.NAME,'submit').click()#立即登录
        a1=self.driver.switch_to.alert#切换到消息框
        t1=a1.text#获得消息框里的文本信息
        self.assertIn('用户名不能为空',t1)
        self.assertIn('登录密码不能为空',t1)
        a1.accept()#点击“确定”按钮关闭它


if __name__ == '__main__':
    unittest.main()
