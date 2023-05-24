import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MyTestCase(unittest.TestCase):
    def test_3(self):
        #driver=webdriver.Firefox()
        self.driver.get('http://localhost/upload/index.php')#首页
        self.driver.find_element(By.NAME,'imageField').click()
        sleep(4)
        #self.driver.quit()

    def tearDown(self):
        self.driver.quit()

    def test_1(self):
        #driver=webdriver.Firefox()
        self.driver.get('http://localhost/upload/index.php')#首页
        self.driver.find_element(By.ID,'keyword').send_keys('806')#关键字
        self.driver.find_element(By.NAME,'imageField').click()#搜索
        sleep(4)
        # 检查排序的第一个下拉列表里默认选项文本是“按上架时间排序”
        s1=Select(self.driver.find_element(By.NAME,'sort'))
        t1=s1.first_selected_option.text#first_selected_option只获得默认选项（元素对象），用.text才能获得选项的文本（str）
        self.assertEqual('按上架时间排序',t1)
        # 练习：检查排序的第二个下拉列表里默认选项文本是“倒序”
        s2=Select(self.driver.find_element(By.NAME,'order'))
        t2=s2.first_selected_option.text
        self.assertEqual('倒序',t2)
        # 检查排序的第二个下拉列表里选项的总个数是2
        all=s2.options
        count=len(all)
        self.assertEqual(2,count)#注意：预期值是int类型
        # 检查关键字文本框里保留原来所输入的那个数据“806”
        v1=self.driver.find_element(By.ID,'keyword').get_attribute('value')
        self.assertEqual('806',v1)
        #self.driver.quit()

    def test_2(self):
        #driver=webdriver.Firefox()
        self.driver.get('http://localhost/upload/index.php')#首页
        self.driver.find_element(By.ID,'keyword').send_keys('abcde')#关键字
        self.driver.find_element(By.NAME,'imageField').click()
        sleep(4)
        # 检查搜索结果里的提示信息是“无法搜索到您要找的商品！”
        m=self.driver.find_element(By.CLASS_NAME,'f5').text
        self.assertEqual('无法搜索到您要找的商品！',m)
        # 检查总计的记录数是0
        c=self.driver.find_element(By.XPATH,'//div[@id="pager"]/span/b').text
        self.assertEqual('0',c)#注意：text得到的文本是str类型
        #self.driver.quit()

    def setUp(self):
        self.driver = webdriver.Firefox()

if __name__ == '__main__':
    unittest.main()
