person = {
    'firstname': 'John',
    'lastname': 'Doe',
    'age': 30
 }

 #using constructor

#person2 = dict(first_name='Sara',last_name='William')

print(person)

#get value
print(person['firstname'])
print(person.get('lastname')) 

person['phone']='555-555'
print(person.keys())
print(person.items())

person2 = person.copy()  

del(person['age'])
person.pop('phone')

print(person)

#list of dict

people =[
    {'name': 'eiman', 'age': 30},
    {'name': 'ken', 'age': 10}
]

print(people[2]['name'])
 

