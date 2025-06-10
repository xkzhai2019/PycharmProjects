# coding:utf-8

class Cat(object):
    __cat_type = 'cat'
    def __init__(self,name,sex):
        self.name = name
        self.__sex = sex

    def run(self):
        ret = self.__run()
        print(ret)

    def __run(self):
        return f'{self.__cat_type}, 小猫{self.name}  {self.__sex}开心的奔跑'

    def dump(self):
        ret = self.__dump()
        print(ret)

    def __dump(self):
        return f'{self.__cat_type}, 小猫{self.name}  {self.__sex} 开心的跳'

class Test(object):
    pass

cat = Cat('迷离','female')
cat.run()
cat.dump()
# 私有函数不可以通过实例化对象调用
# cat.__run()

print(dir(cat))
print(cat._Cat__dump()) # 只是被隐藏了，想调用的话
print(cat._Cat__sex)