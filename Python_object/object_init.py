# coding:utf-8
def sleep2(name):  # 内部函数可以不用self关键字
    return name
class Person(object):
    name = None
    age = None

    def run(self):
        print(f'{self.name} 在奔跑' )

    def jump(self):
        print(f'{self.name} 在跳')

    def sleep(): # 成员函数必须有self关键字
        print('sleep')

    def work(self):
        self.run()
        self.jump()
        def sleep(name): # 内部函数可以不用self关键字
            return name
        ret = sleep2(self.name)
        print('sleep ret is ',ret)
xiaomu = Person()
xiaomu.run()
xiaomu.name = 'xiaomu'
xiaomu.jump()

dwei = Person()
dwei.jump()

dwei.top = 174
print(dwei.top)

#print(xiaomu.top)

print(dwei.age)
print('---------')
xiaomu.work()
#xiaomu.sleep()

print('----------')
class Person2(object):
    def __init__(self,name,age=None):
        self.name = name
        self.age = age
    def run(self):
        print(f'{self.name} 在奔跑' )

    def jump(self):
        print(f'{self.name} 在跳')
    def work(self):
        self.run()
        self.jump()

xiaomu = Person2(name='xiaomu',age=10)
xiaomu.jump()
xiaomu.name='小木'
xiaomu.jump()
