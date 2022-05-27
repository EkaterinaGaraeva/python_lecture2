# Кортежи

(a) = (3, 1, 41, 4)
print(a)
print(a[0]) # 3
print(a[-1]) # 4
print(a[-2]) # 41

b = (3,) # кортеж из одного элемента

d = (3, 4, 5)
for item in d:
    print(item)


t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r: {} g: {} b: {}'.format(red, green, blue))
# r: red g: green b: blue
