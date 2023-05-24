class Cal:
    # 构造函数，初始化两个参与计算的数据
    def __init__(self,x,y):
        self.x=x
        self.y=y
    # 加法计算：计算两个数据的和，返回
    def add(self):
        result1=self.x+self.y
        return result1
    # 减法计算：计算两个数据的差，返回
    def sub(self):
        result2=self.x-self.y
        return result2