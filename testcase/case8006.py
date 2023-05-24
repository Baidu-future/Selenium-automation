import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    # 自定义方法：通用
    # 名称：is_element_present，不要以test_开头
    # 功能：判断符合特定条件的元素是否出现在当前网页里（也就是是否能定位成功）
    # 参数：定位条件，包含how代表怎么定位（值是By.XXX）、what代表用什么定位（值是定位用的字符串数据）
    # 返回值：True代表定位成功(出现)，False代表定位失败（未出现或已经消失）
    def is_element_present(self,how,what):
        try:
            self.driver.find_element(how,what)
            return True
        except NoSuchElementException:
            return False

    def test_1(self):
        self.driver.get('http://localhost/upload/index.php')
        self.driver.find_element(By.ID,'keyword').send_keys('806')#关键字
        self.driver.find_element(By.NAME,'imageField').click()#搜索
        sleep(3)
        # 检查P806的商品名称出现在当前网页里
        result1=self.is_element_present(By.LINK_TEXT,'P806')
        self.assertTrue(result1)

    def test_2(self):
        self.driver.get('http://localhost/upload/index.php')#首页
        # 点击“高级搜索”
        self.driver.find_element(By.LINK_TEXT,'高级搜索').click()
        # 等待4秒
        sleep(4)
        # 选择“扩展选项”下拉列表里的“精品手机”这个选项
        Select(self.driver.find_element(By.NAME,'goods_type')).select_by_visible_text('精品手机')
        # 等待4秒
        sleep(4)
        # 检查“内存容量”第一个文本框出现在当前网页里
        result21=self.is_element_present(By.NAME,'attr[181][from]')
        self.assertTrue(result21)
        # 检查“颜色”下拉列表出现在当前网页里
        result22=self.is_element_present(By.NAME,'attr[185]')
        self.assertTrue(result22)


if __name__ == '__main__':
    unittest.main()
