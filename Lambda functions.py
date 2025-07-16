#Lambda functions in python are small anonymous functions defined using the lambda keyword

#usual code
def addition(a,b):
    return a+b
a=addition(2,3)
print(a)

#using lambda function
addition= lambda a,b:a+b
print(type(addition))
print(addition(2,3))

#even odd code
even= lambda num:num%2==0
print(even(6))
