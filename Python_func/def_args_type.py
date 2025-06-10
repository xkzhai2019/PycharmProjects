# coding: utf-8

def add(a:int,b:int=2):
    print(a+b)

add(1,2)
add('hello','xiaomu') # 不会进行验证，只是说明

def test(a:int,b:int=3,*args:int,**kwargs:str):
    print(a,b,args,kwargs)

test(1,2,3,'42',name='xiaomu')

def test2(a:int,b,c=3):
    print(a,b,c)

test2(1,3,4)