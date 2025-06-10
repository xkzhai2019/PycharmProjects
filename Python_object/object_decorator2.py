# coding: utf-8
class Test(object):
    def __init__(self,a):
        self.a = a

    def run(self):
        print('run')
        self.dump()
        self.sleep() #普通类函数调用cls static 函数

    @classmethod
    def dump(cls):
        print('dump')
        #cls.run() # 无法通过cls调用self

    @staticmethod
    def sleep():
        print('I want sleep')


t = Test('a')
t.run()

#Test.run()
#Test.dump()
print('----------')
Test.sleep()
t.sleep()
t.dump()
print('----------')
class Test2(object):
    def __init__(self,name):
        self.__name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value

t1 = Test2('deweo')
print(t1.name)

t1.name = 'xiaomu'
print(t1.name)
# t1.name = 'xiaom'
# print(t1.name)
