#simple calculator using if,else and elif condition
num1=float(input('enter any number:'))
num2=float(input('enter any number:'))
operation=input('enter operation(+,-,*,/)')

if operation=='+':
    print(num1+num2)
elif operation=='-':
    print(num1-num2)
elif operation=='*':
    print(num1*num2)
elif operation=='/':
    print(num1/num2)
    if num2==0:
        print('cannot divide by zero')
    else:
        print(num1/num2)
else:
    print('something went wrong')


