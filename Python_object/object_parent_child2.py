# coding: utf-8
# 1. 定义两个父类

class Food(object):
    def work(self):
        return 'food work'
    def cake(self):
        return 'I like cake'

class Tools(object):
    def work(self):
        return 'tool work'

    def car(self):
        return 'car will run'


# 2. 继承父类的子类
class Person(Food,Tools): # 继承顺序：从左往右
    pass

if __name__=='__main__':
    p = Person()
    p_car = p.car()
    p_cake = p.cake()
    p_work = p.work()
    print(p_car)
    print(p_cake)
    print(p_work)
    print(Person.__mro__)