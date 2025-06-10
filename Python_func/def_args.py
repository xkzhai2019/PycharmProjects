# coding: utf-8

# a,b为必传参数,c为默认参数
def add(a,b,c=3):
    return a+b+c

ret = add(1,2)
print(ret)

ret = add(1,2,6)
print(ret)

# 可变参数
def test_args(*args,**kwargs):
    print(args,type(args))
    print(kwargs,type(kwargs))

test_args(1,2,3,4,5,6,name='lisi',age=3)

def test_args_supper(*args,**kwargs):
    if len(args)>=1:
        print(args[0])
    if 'name' in kwargs:
        print(kwargs['name'])
    else:
        print('no name')
    print(args,len(args))
    print(kwargs,len(kwargs))

test_args_supper(1,name='xkzhai')

a = ('python','django') # 元组
b = {'name': 'xkzhai'} # 字典
test_args_supper(a,b)
test_args_supper(*a,**b)


print('---------------')
def add(a,b=1):
    return a+b

print(add(1,2))
print(add(1))
print(add(a=1,b=2))
print(add(b=2,a=1))
# print(add(b=2)) #a是必传参数

def test(a,b=1,*args):
    print(a,b,args)
s = (1,2)
test(1,2,*s)
#test(a=1,b=2,(1,2))

def test2(*args,a,b=1):
    print(a,b,args)
test2(a=1,b=2,*s) # 不推荐

def test3(a,b=1,**kwargs):
    print(a,b,kwargs)

test3(1,2,name='xkzhai')
test3(a=1,b=2,name='xkzhai')
test3(name='xkzhai',age=33,a=1, b=2)


d = {'name':'xiaomu'}
test3(a=1,b=2,**d)
test3(**d,a=1,b=2)
# test3(**d,1,2)

