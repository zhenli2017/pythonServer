# -*- coding: utf-8 -*

import os

# 数据库
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456qQ0@39.96.41.103:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 无参数函数
def demo1():
    print "Demo 1"


# 检查类型函数
def demo2(a):
    if not isinstance(a, (int, float)):
        raise TypeError("类型不对,需要 int float")
    else:
        # 返回多个值,实际上是一个tuple
        print "a = %s", a


# 默认参数
def demo3(name, age=20):
    print "name = " + name + " age = " + age


def demo4(l=None):
    # 默认参数一定要指向不可变的对象
    print l


# 可变参数
def demo5(*numbers):
    for n in numbers:
        print "n = " + n


# 关键字函数
def demo6(**kw):
    print "关键字函数 = ", kw


# 切片
def demo7():
    print "==== 切片 ===="
    demo7List = [4, 5, 6, 7, 8, 9, 0]
    print demo7List
    print "取前三个", demo7List[0:3]
    print "取后三个", demo7List[-3:]
    print "前5个每隔2个取一个", demo7List[:5:2]
    print "复制一个list", demo7List[:]


# 列表生成式
def demo8():
    print "==== 列表生成式 ===="
    # m+n : 具体执行内容,后面 for 循环 ,最后面加 if 判断
    demo8List = [m + n for m in "ABC" for n in "abc" if m != "A"]
    print demo8List


# 文件读取
def demo9():
    print "==== 文件IO ===="
    with open("/Users/wo/Downloads/6201001000004_2018_10_24.log", "rw") as demo9File:
        demo9List = range(10)
        for n in range(10):
            demo9List[n] = demo9File.readline()
        print demo9List
        print demo9List


# 操作目录
def demo10():
    print "==== 操作目录 ==== "
    print os.name
    print "查看当前目录的绝对路径 = ", os.path.abspath(".")
    print "创建一个目录"
    os.path.join("/Users/wo/Desktop", "aa")
    # 创建文件夹
    # os.mkdir("/Users/wo/Desktop/aa")
    # 删除文件夹
    # os.rmdir("/Users/wo/Desktop/aa")
    # 获取目录和文件名
    dirRoot = "/Users/wo/Desktop/PyCharm/demo1"
    for dirName in os.listdir(dirRoot):
        if dirName == "demo1":
            dirRoot = dirRoot + "/" + dirName
            dirList = os.listdir(dirRoot)
            for fileName in dirList:
                print "目录和文件名分离 = ", os.path.split(dirRoot + "/" + fileName)
                print "文件名和扩展名分离 = ", os.path.splitext(dirRoot + "/" + fileName)


# 数据库操作
def demo11():
    session = DBSession()
    newUser = User("100", "name")
    session.add(newUser)
    session.commit()
    session.close()
    pass


# demo1()
# demo2(100)
# # demo2("ppp")
#
# demo4List = [1, 2, 3, 4, 5, 6, 7]
# demo4(demo4List)
#
# demo6Dict = {"name": "a", "age": 100}
# demo6(**demo6Dict)
#
# demo7()
# demo8()
# demo9()
# demo10()
demo11()
