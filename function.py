#create

def sayhello(name = 'Sam'):
    print(f'Hello {name}')

#ccalling function
#sayhello()

#return values
def getsome(num1,num2):
    total=(num1+num2)
    return total

print(getsome(3,5))

#lambda function is a small anonymous function can take num of argumens. 
# but only one expression

getsum = lambda num1,num2 : num1 + num2

print(getsum(10,3))
