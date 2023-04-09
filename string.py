name = 'Brad'
age = 27

#concatenate
print('Hello, my name is ' + name + ' and my age is '+ str(age))

#String formatting

#arguments by position
print('my name is {name} and I am {age}'.format(name=name, age=age))

#f-string
print(f'hello,my name is {name} and i am {age}')

#String methods


#Capitalize

s = 'helloworld'
print('s=hello world')
print(s.capitalize())
print(s.upper())
print(s.swapcase())
print(len(s))
print(s.replace('world','everyone'))
sub = 'h'
print(s.count(sub ))
print(s.split())
print(s.find('r'))
print(s.isalnum())
print(s.isnumeric())

 