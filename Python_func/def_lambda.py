# coding:utf-8

f = lambda : print(1)
f()
#print(ret)

f1 = lambda x,y=2: x>y
print(f1(3))

users = [
    {'name':'xkzhai'},
    {'name': 'dewei'},
    {'name': 'asan'}
]

users.sort(key=lambda x: x['name'])
print(users)