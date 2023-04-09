#tuple is unchangeable, no duplicate membrs

fruits  = ('apple','oranges','grapes')
fruits2 = tuple(('apples','oranges','grapes'))

#single value needs trailing comma
fruits2 = ('apples',)

print(fruits[1])

#cant
#fruits[0] = 'pears'

del fruits2

print(fruits2, type(fruits2))