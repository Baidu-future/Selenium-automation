import unittest
from testcase.case6006 import MyCalTestCase
from testcase.case6007 import MyTestCase

s1=unittest.TestSuite()#创建一个空测试套件
s1.addTest(MyCalTestCase('test_add_1'))#加一条测试用例
s1.addTest(MyCalTestCase('test_add_2'))#加一条测试用例
s1.addTest(MyTestCase('test_1'))#加一条测试用例
s1.addTest(MyTestCase('test_2'))#加一条测试用例
#……
r1=unittest.TextTestRunner()#创建一个测试运行器
r1.run(s1)#调用run方法来运行，参数是测试套件对象
