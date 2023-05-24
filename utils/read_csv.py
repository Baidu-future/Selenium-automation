import csv


class CSVUtil:

    #构造函数：初始化，准备csv数据文件的路径
    def __init__(self,file_path):
        self.file_path=file_path

    # 读取csv文件里的数据，以list类型（每个成员还是一个list类型的数据，小列表代表一行数据，大列表代表整个csv里的所有数据）返回
    def get_list_data(self):
        value=[]
        f=open(self.file_path,'r',encoding='utf-8')
        c=csv.reader(f)
        next(c)#跳过第一行（因为第一行是注释）
        for row in c:
            value.append(row)#r是列表，代表一行数据
        f.close()
        return value#value是列表，代表一整个csv里的所有数据


# 调试当前类
if __name__ == '__main__':
    u=CSVUtil('..\\testdata\\data1.csv')
    d=u.get_list_data()
    print(d)