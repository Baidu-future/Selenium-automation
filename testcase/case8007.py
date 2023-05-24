import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    # 自定义方法
    # 功能：判断是否出现消息框
    # 参数：无
    # 返回值：布尔值，True代表出现消息框，False代表没有消息框
    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
            return True
        except NoAlertPresentException:
            return False

    # 自定义方法：通用
    # 功能：切换到消息框、获得文本、点击消息框里的按钮
    # 参数：is_accept是布尔值，可选，默认值是True代表点击“确定”，如果是False代表点击“取消”
    # 返回值：消息框文本（str）
    def close_alert(self,is_accept=True):#is_accept默认值是True
        a1=self.driver.switch_to.alert
        t1=a1.text
        if is_accept:
            a1.accept()#点击“确定”
        else:
            a1.dismiss()#点击“取消”
        return t1

    # def test_1(self):
    #     self.driver.get('http://localhost/upload/index.php')#前台首页
    #     self.driver.find_element(By.NAME,'imageField').click()#搜索
    #     sleep(3)
    #     # 检查消息框出现（弹出来）
    #     result11=self.is_alert_present()
    #     self.assertTrue(result11)
    #     # 切换到消息框
    #     a1=self.driver.switch_to.alert
    #     # 获得消息框里的文本信息
    #     t1=a1.text
    #     # 检查信息等于“请输入搜索关键词！”
    #     self.assertEqual('请输入搜索关键词！',t1)
    #     # 点击消息框里的“确定”按钮
    #     a1.accept()
    #     # 检查消息框已经消失
    #     result12=self.is_alert_present()
    #     self.assertFalse(result12)

    def test_1(self):
        self.driver.get('http://localhost/upload/index.php')#前台首页
        self.driver.find_element(By.NAME,'imageField').click()#搜索
        sleep(3)
        # 检查消息框出现（弹出来）
        result11=self.is_alert_present()
        self.assertTrue(result11)
        # 调用自定义方法，完成消息框操作
        t11=self.close_alert()
        # 检查信息等于“请输入搜索关键词！”
        self.assertEqual('请输入搜索关键词！',t11)
        # 检查消息框已经消失
        result12=self.is_alert_present()
        self.assertFalse(result12)

if __name__ == '__main__':
    unittest.main()
