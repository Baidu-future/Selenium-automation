
from selenimport unittestium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from ddt import ddt,data,unpack
from utils.read_csv import CSVUtil

# 读取csv文件里的数据
u = CSVUtil('..\\testdata\\data1.csv')
d = u.get_list_data()
print(d)

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(14)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    @data(*d)
    @unpack
    def test_something(self,min,max,out):
        print(min,max,out)
        self.driver.get('http://localhost/upload/index.php')#前台首页
        self.driver.find_element(By.LINK_TEXT,'高级搜索').click()
        sleep(3)
        self.driver.find_element(By.ID,'min_price').send_keys(min)#输入价格最小值
        self.driver.find_element(By.ID,'max_price').send_keys(max)#输入价格最大值
        # 判断测试数据里“隐藏已脱销的商品”复选框准备的值是否等于ON，如果等于，就点击一下该复选框。否则，就不做任何处理。
        if out=='ON':
            self.driver.find_element(By.ID,'outstock').click()
        sleep(4)
        self.driver.find_element(By.NAME,'Submit').click()#立即搜索
        sleep(2)


if __name__ == '__main__':
    unittest.main()
