import unittest
from testcase.case6006 import MyCalTestCase
from testcase.case6007 import MyTestCase
from utils.HTMLTestRunner1 import HTMLTestRunner

s1=unittest.TestSuite()#创建一个空测试套件
s1.addTest(MyCalTestCase('test_add_1'))#加一条测试用例
s1.addTest(MyCalTestCase('test_add_2'))#加一条测试用例
s1.addTest(MyTestCase('test_1'))#加一条测试用例
s1.addTest(MyTestCase('test_2'))#加一条测试用例
# 打开测试结果报告文件
# open函数第一个参数是文件路径（支持绝对路径和相对路径），文件夹不存在会报错，文件不存在时，会自动创建文件。
# open函数第二个参数是wb代表以二进制模式写数据到文件
h=open('..\\report\\测试结果报告.html','wb')
# 创建HTMLTestRunner对象（实例化）
r1=HTMLTestRunner(h)#构造函数的参数是已经打开的文件对象
r1.run(s1)#调用run方法运行测试套件，参数是测试套件对象
h.close()#关闭文件