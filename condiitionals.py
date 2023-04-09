x = 3
y = 5

if x>y:
    print(f'{x} is greater than {y}')

elif y>x:
    print(f'{y} is greater')

else:
    print('both are equal')


#nested if
if x>2:
    if x<=10:
        print('ok')

#also
if x>2 and x<=10:
    print('right')

if not(y==x):
    print('not opeator')
     

#Membership operator

numbers = [1,2,4,5]

#if x in numbers:
 #   print(x in numbers)

if x not in numbers:
    print(x not in numbers)


# is (identity )

if x is not y:
    print(f'{x} is not {y}')

