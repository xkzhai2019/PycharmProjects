# coding: utf-8

class Parent(object):
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

    def talk(self):
        return f'{self.name} are talking'

    def is_sex(self):
        if self.sex == 'boy':
            return f'{self.name} is a boy'
        else:
            return f'{self.name} is a girl'

class Childone(Parent):
    def play_football(self):
        return f'{self.name} are playing football'
class ChildTwo(Parent):
    def play_pingpang(self):
        return f'{self.name} are playing pingpang'

c_one = Childone(name='xiaomu',sex='boy')
ret = c_one.play_football()
print(ret)
c_two = ChildTwo(name='xiaoyun',sex='girl')
ret = c_two.play_pingpang()
print(ret)

p = Parent(name='dad',sex='boy')
ret = p.talk()
print(ret)

ret=p.is_sex()
print(ret)
ret = p.playpang() # 父类无法调用子类的方法

