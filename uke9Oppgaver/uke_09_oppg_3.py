# skrive ut keys og values til en dictionary i tilleg til i en liste

myDictionary = {0: 0, 1: 'vafler', 'two': 2, 5: 4}
myList = [0, 1, 'boller', 4]

print('Dictionary Keys:')
for key in myDictionary.keys():
    print(key)

print('')

print('Dictionary Values:')
for value in myDictionary.values():
    print(value)

print('')

print('Dictionary keys/value:')
for key, itemValue in myDictionary.items():
    print(key, itemValue)

print('')

print('List values:')
for items in myList:
    print(items)

print('')

print('List indices/value:')
for i, v in enumerate(myList):
    print(i, v)