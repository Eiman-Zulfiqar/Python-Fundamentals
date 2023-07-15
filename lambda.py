# def double(x):
#     return x*2

# variable of function

def apply(fx, value):
    return 6 + fx(value)

#or

print(apply(lambda x: x*x*x, 2))

double = lambda x: x*2

cube = lambda x: x*x*x

avg = lambda x,y: (x+y)/2

print(double(5))

print(cube(5))

print(avg(2,8))

print(apply(cube,2))

