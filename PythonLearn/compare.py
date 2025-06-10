# coding:utf-8

a = 1
b = 2.2
c=  0
d = 18
e = -3
f = 300

print(a==b)
print(a!=b)
print(a<b)
print(a>e)
print(d>=b)

d01 = 18
print(d>=d01)
print(d is d01)
print('d id is:', id(d))
print('d01 id is:', id(d01))

f01 = 300
print(f==f01)
print(f is f01)

print(f is d)
print(id(f))
print(id(d))
print(f is not d)