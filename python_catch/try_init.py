# coding: utf-8

def upper(str_data):
    new_str = 'None'
    try:
        new_str = str_data.upper()
    except Exception as e:
        print('程序出错了:{}'.format(e))
    return new_str

ret = upper('dewei')
print(ret)

ret = upper(1)
print(ret)


def test():
    try:
        print('1/0:')
        1 / 0
        print('hello')
    except ZeroDivisionError as e:
        print(e)
test()

def test1():
    try:
        print('hello')
        print(name)
    # except ZeroDivisionError as e: # 异常不匹配
    # except Exception as e:
    except (ZeroDivisionError,NameError) as e:
        print(e)
        print(type(e))
        print(dir(e))
test1()
