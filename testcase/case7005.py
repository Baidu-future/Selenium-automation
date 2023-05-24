import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
# 导入ddt里的三个装饰器
from ddt import ddt,data,unpack

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(14)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    @data(['a','4'],['b','1'],['c','24'])
    @unpack
    def test_search(self,k,e):
        print(k,e)
        self.driver.get('http://localhost/upload/index.php')#前台首页
        self.driver.find_element(By.ID,'keyword').send_keys(k)#关键字
        self.driver.find_element(By.NAME,'imageField').click()#搜索
        sleep(4)
        # 检查总计记录数等于预期值
        a=self.driver.find_element(By.XPATH,'//div[@id="pager"]/span/b').text
        self.assertEqual(e,a)#此处，e变量必须是str类型才行



if __name__ == '__main__':
    unittest.main()
