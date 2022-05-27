# Словари

dictionary = {}
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться

for k in dictionary.keys():
    print(k)

for j in dictionary.values():
    print(j)

for v in dictionary:
    print(v)

print(dictionary['up'])
dictionary['up'] = 'up'
print(dictionary['up'])
