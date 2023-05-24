import unittest


class MyTestCase(unittest.TestCase):
    def test_1(self):
        a=20
        b=3
        self.assertAlmostEqual(6.67,a/b,2)#四舍五入精确到小数点后2位

    def test_2(self):
        a='e8'
        b='hello'
        self.assertIn(a,b,msg='a没有被包含在b里')#故意制造的失败
        c=8
        d=[2,6,8,10]
        self.assertIn(c,d)

    def test_3(self):
        a='hello world'
        b='hel'
        c='rld'
        self.assertTrue(a.startswith(b))#a的开头部分是b
        self.assertTrue(a.endswith(c))#a结尾部分是c
        self.assertFalse(a.startswith(c))#a的开头部分不是c
        d=10
        e=20
        f=5
        self.assertTrue(d<e and d>f)
        g=len(a)
        self.assertTrue(g>1 and g<20)


if __name__ == '__main__':
    unittest.main()
