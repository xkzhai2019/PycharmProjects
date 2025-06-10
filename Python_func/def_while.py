# coding: utf-8

count = 0

def test():
    global count
    count += 1

    if count !=5:
        print('当前count是%s，count条件不满足，重新执行自己' % count)
        return test()
    else:
        print('count is %s' %count)

test()