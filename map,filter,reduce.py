def cube(x):
    return x*x*x

# print(cube(2))

l = [1, 2 , 3 , 4]
# newl = []

# for item in l:
#     newl.append(cube(item))
newl = list(map(cube,l))
print(newl)

#filter only those elements which qualify

def filter_function(a):
    return a>4

newnewl = list(filter(filter_function, newl))
print(newnewl)

from functools import reduce

numbers = [1,2,3,4,5]

def product(x,y):
    return x * y

sum = reduce(product, numbers)

print(sum)