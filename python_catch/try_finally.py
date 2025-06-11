# coding: utf-8

def test1():
    try:
        1/0
    except Exception as e:
        print(e)
    finally:
        return 'finally'

ret =test1()
print(ret)
print('--------------')

def test2():
    try:
        1/0
    except Exception as e:
        print('11111')
        return  e
    finally:
        print('finally')

ret = test2()
print(ret)
print('----------')
def test3():
    try:
        print('try test 1111')
        return 'try'
    except Exception as e:
        print(e)
    finally:
        print('finally e')
ret = test3()
print(ret)
print('----------')

def test4():
    try:
        1/0
    except Exception as e:
        print('1')
        return e
    finally:
        print('2')
        return 'finally'

ret = test4()
print(ret)
print('---------------')

def test5():
    try:
        print('11111try')
        return 'try'
    except Exception as e:
        print('e')
    finally:
        print('222222')
        return 'finally'

ret = test5()
print(ret)

def test6():
    try:
        print('try1')
        1/0
        print('try3')
    finally:
        return 'i am finally'
print('---------')
ret = test6()
print(ret)