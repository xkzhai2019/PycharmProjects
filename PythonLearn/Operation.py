# coding:utf-8


a = 1
b = 2
c = 3

d = a+b+c
d  += c
print(d)

d -= a
print(d)

d *= b # d = d*b
print(d)

a //= b
print(a)

c %= 3
print(c)

f = 10
f **= 2
print(f)


list01 = [1,2,3]
print(list01*2)

tuple01 = (1,2,3)
print(tuple01*2)

# 字典不支持乘法运算
# dist01 = {'name':'kai'}
# print(dist01*2)
