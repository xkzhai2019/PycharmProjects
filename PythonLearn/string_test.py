name = 'xkzhai'
name_02 = '木木'

print(id(name))
print(id(name_02))


new_name = name
print(id(new_name))

info = '''
        今天的天气真好
    '''
print(info)

info1 = 'abdf'
info2 = "abdf"
new_str = 'nihao xkzhai "mumu"'
print(new_str)

print(id(info1))
info1 = info1 + info2
print(id(info1))