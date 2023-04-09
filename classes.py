#class is used for creating objects

#create class
class User:
    #constructor: function which run 
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def has_birthday(self):
        self.age += 1

#Extend class
class Customer(User):
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self,balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'



#init user object
eiman = User('EIMAN ZULFIQAR','iemanzulfiqar05@gmail.com',21)
eiman2 = User('Eshal asim', 'abx@haha', 18)
jannet = Customer('jannet', 'jannet@33', 35)

jannet.set_balance(50)
print(jannet.greeting())




eiman2.has_birthday()
print(eiman2.greeting())
print(type(eiman))

