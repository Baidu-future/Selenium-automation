import unittest
from utils.HTMLTestRunner1 import HTMLTestRunner

# 测试用例的代码文件所在的路径
file_path='..\\testcase'
# 测试用例的代码文件的名称规则(例如：以case开头的python文件)
# *代表任意字符串
file_name='case*.py'
# TestLoader类里的discover方法，负责找指定路径下的所有符合规则的文件，加载这些文件里的所有用例到一个测试套件里，返回该测试套件
s1=unittest.defaultTestLoader.discover(file_path,file_name)

# 打开测试结果报告文件
# open函数第一个参数是文件路径（支持绝对路径和相对路径），文件夹不存在会报错，文件不存在时，会自动创建文件。
# open函数第二个参数是wb代表以二进制模式写数据到文件
h=open('..\\report\\测试结果报告.html','wb')
# 创建HTMLTestRunner对象（实例化）
r1=HTMLTestRunner(h)#构造函数的参数是已经打开的文件对象
r1.run(s1)#调用run方法运行测试套件，参数是测试套件对象
h.close()#关闭文件