# it is just like array, changeable, allow duplicate memebers

numbers = [1,2,3,4,5]
fruits = ['apples','mangoes','oranges','peaches']
#using constructor
#numbers2 = list((1,2,3,4,5))

#get a single value
print(fruits[1:3])
print(len(fruits))
fruits.append('grapes')
fruits.remove('mangoes')
fruits.insert(2, 'Strawberries')


fruits.pop(2)
fruits.reverse()
fruits.sort()
fruits.sort(reverse=True)
fruits[0]='blueberries'
print(fruits)

data = [1, 'abc', 'zxc', 3.24]

print(data, type(data))
print(type(data[2]))
