# coding:utf-8

a = set()
print(a)
print(type(a))

b = set(['python','django','flask'])
print(b)

#c = {[1,2,3]}
c = {(1,2,3),'123',1,'123'}
print(c)

d = {}
print(d,type(d))

a_list = ['python','django','flask']
b_set = set(a_list)
print(b_set)