# coding: utf-8

def capitalize(data):
    index = 0
    temp = ''

    for item in data:
        if index==0:
            temp = item.upper()
        else:
            temp += item
        index += 1
    print('for is over')
    return temp
    print('finish')

#ret = capitalize(data=123)
ret = capitalize(data="hello xkzhai")
print(ret)

def message(message, message_type):
    new_message = '[%s] %s' % (message_type,message)
    print(new_message)

ret = message(message='weather is good',message_type='info')
print('message ret',ret)


def test():
    for i in range(10):
        if i==5:
            return i
print('test is: ',test())