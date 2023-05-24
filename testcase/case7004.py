import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(12)#隐式等待
        self.driver.maximize_window()#最大化

    def tearDown(self):
        self.driver.quit()

    def test_1(self):
        self.driver.get('http://localhost/upload/goods.php?id=24')#打开P806商品的详情页
        # 检查购买数量文本框里的默认值是1
        n=self.driver.find_element(By.ID,'number').get_attribute('value')
        self.assertEqual('1',n)#注意：预期值是str类型
        # 检查灰色单选按钮默认已经被选中
        s1=self.driver.find_element(By.ID,'spec_value_167').is_selected()
        self.assertTrue(s1)
        # 检查数据线复选框默认没有被选中
        s2=self.driver.find_element(By.ID,'spec_value_168').is_selected()
        self.assertFalse(s2)
        # 练习：检查当前界面下方的评价等级里，第五个单选按钮默认是被选中的
        s3=self.driver.find_element(By.ID,'comment_rank5').is_selected()
        self.assertTrue(s3)
        # 检查当前界面下方的评价等级单选按钮一共有5个
        list1=self.driver.find_elements(By.NAME,'comment_rank')
        count=len(list1)
        self.assertEqual(5,count)#注意：预期值是int类型

    # 练习：新建test_2，打开注册页，检查加密的文本框有2个
    def test_2(self):
        self.driver.get('http://localhost/upload/user.php?act=register')
        list2=self.driver.find_elements(By.XPATH,'//input[@type="password"]')
        count2=len(list2)
        self.assertEqual(2,count2)


if __name__ == '__main__':
    unittest.main()
