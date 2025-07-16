'''Introduction to Functions- a funtion is a block of code that performs a specific
task. funtion helps in organizing code, reusing code and improving readability'''

#Syntax
def function_name(parameters):
    '''docstring''' #docstring is basically like comments, it is not necc to write it
        #funtion body
        #return statement

#why functions are used? eg below
num=24
if num%2==0:
    print(True)
else:
    print(False)

#but if we use functions
def even(num):
    if num%2==0:
        return True
    else:
        return False
even_odd=even(26) # now here this even odd funtion is stored in a function named as 'even', so whenever we need to check if te number is odd or even, just call the function
print(even_odd)

#Functions w multiple parameters
def add(a,b):
    return a+b
addition=add(2,3)
print(addition)

#Default parameters
def greet(name):
    print(f"Hello {name} Welcome to the paradise")
s=greet('shreyas')
#this is a usual code

#if the user does'nt give the name, then by default 'guest' should be returned

def greet(name='Guest'):
    print(f"Hello {name} Welcome to the paradise")
greet()

#Variable length arguments
#1) postional argument
def print_num(*args):
    for number in args:
        print(number)

print_num(1,2,'shreyas') #basically multiple parameters can be passed

#the above code can also be written as
def print_num(*args):
    print(args)

print_num(1,2,'shreyas')# args-arguments, while defining the function '*' is written before it coz syntax is like that - function(*args)

#2)keyword argument
def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_details(name='shreyas',age=20)#basically multiple parameters can be passed in key-value pair, syntax-function(**kwargs)

#3) for both positional/keyword argument
def both(*args,**kwargs):
    for number in args:
        print(number)
    for key,value in kwargs.items():
        print(f"{key}:{value}")
both(1,2,3,name='shreyas',age=20) #combination of both

#Returning multiple parameters
def mul(a,b):
    return a*b,a,b
m=mul(2,3)
print(m)
    
