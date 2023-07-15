# class Person:
#     name = "Harry"
#     occupation = "Software developer"
#     networth = 10

#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# # no need to right new keyword
# a=Person()
# a.name = "Eiman"
# a.occupation = "web developer"
# b=Person()
# b.name = "abc"
# b.occupation = "HR"

# # print(a.name,a.occupation,a.networth)

# a.info()
# b.info()

#constructor

class Person:
    def __init__(self, name, occupation):
        print("I am a person")
        self.name = name
        self.occupation = occupation
    
    def info(self):
         print(f"{self.name} is a {self.occupation}")


a = Person("harry","dev")
b= Person("eiman", "hr")

a.info()