# coding: utf-8

def upper(str_data):
    new_str = 'None'
    try:
        new_str = str_data.upper()
    except:
        print('程序出错了')
    return new_str

ret = upper('dewei')
print(ret)

ret = upper(1)
print(ret)