import unittest
from utils.HTMLTestRunner1 import HTMLTestRunner

# 加载测试用例到测试套件里
file_path='..\\testcase'
file_name='case8*.py'
s1=unittest.defaultTestLoader.discover(file_path,file_name)
# 运行测试套件，生成HTML格式的测试结果报告
h=open('..\\report\\Selenium测试结果报告.html','wb')#以写入模式打开html文件
r1=HTMLTestRunner(h,title='Selenium测试报告')#创建测试运行器对象
r1.run(s1)#运行测试套件
h.close()#关闭html文件