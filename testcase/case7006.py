import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from ddt import ddt,data,unpack

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    @data(['jack@126.com','hello','world'],
          ['zs@163.com','你好','我要采购最新款手机'],
          ['ls@qq.com','询问手机价格','最新款华为手机多少钱'],
          ['rose@gmail.com','hello123','hi'])
    @unpack
    def test_something(self,e,t,c):
        print(e,t,c)
        # 打开留言板页
        self.driver.get('http://localhost/upload/message.php')
        # 输入电子邮件地址
        self.driver.find_element(By.NAME,'user_email').send_keys(e)
        # 输入主题
        self.driver.find_element(By.NAME,'msg_title').send_keys(t)
        # 输入留言内容
        self.driver.find_element(By.NAME,'msg_content').send_keys(c)
        # 点击“我要留言”按钮
        self.driver.find_element(By.XPATH,'//input[@value="我要留言"]').click()
        sleep(1)
        # 检查网页源代码里包含“您的留言已成功发表, 请等待管理员的审核!”
        ps=self.driver.page_source
        self.assertIn('您的留言已成功发表, 请等待管理员的审核!',ps)


if __name__ == '__main__':
    unittest.main()
