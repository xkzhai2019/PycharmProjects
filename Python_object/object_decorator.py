# coding: utf-8


def check_str(func):
    print('func: ', func)
    def inner(*args, **kwargs):
        print('args: ', args, kwargs)
        ret = func(*args,**kwargs)
        if ret == 'ok':
            return 'ret is %s' % ret
        else:
            return 'ret is failed:%s' % ret
    return inner

@check_str
def test(data):
    return data

ret = test(data='no')
print(ret)

ret = test(data='ok')
print(ret)