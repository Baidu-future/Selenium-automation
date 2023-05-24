import unittest
from dev.cal import Cal


# 当前类名MyTestCase可随便修改，但是它需要是unittest里的TestCase类的子类
class MyCalTestCase(unittest.TestCase):

    #测试方法（名称要求以test_开头）
    def test_add_1(self):
        c1=Cal(10, 20)
        a1=c1.add()
        self.assertEqual(30, a1)

    def test_add_2(self):
        c2=Cal(1.04, 2.01)
        a2=c2.add()
        self.assertEqual(3.05, a2)

    def test_sub_1(self):
        c3=Cal(10, 20)
        a3=c3.sub()
        self.assertEqual(-10, a3)

if __name__ == '__main__':
    unittest.main()
