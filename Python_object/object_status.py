# coding: utf-8

# 1. 定义父类
class XiaomuFather(object):
    def talk(self):
        print('小木的爸爸说了一句话')
    def dump(self):
        print('大家都可以跳...')

# 2. 定义子类，继承父类
class XiaomuBrother(XiaomuFather):
    def run(self):
        print('小木哥哥在奔跑...')
    def talk(self):
        print('小木哥哥在说话...')


class Xiaomu(XiaomuFather):
    def talk(self):
        print('小木也可以说话...')
if __name__ == '__main__':
    xiaomu_brother = XiaomuBrother()
    xiaomu_brother.run()
    xiaomu_brother.talk()
    xiaomu_brother.dump()
    father  = XiaomuFather()
    father.talk()
    father.dump()
    xiaomu = Xiaomu()
    xiaomu.talk()
    xiaomu.dump()