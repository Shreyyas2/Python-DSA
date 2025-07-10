ticket_price=100
age=int(input('enter your age:'))
is_student=40
is_senior_citizen=60
if age<=20:
    discounted_price=50
    if age in range(12,19):
        print(' ')

        print('student ticket fare:',is_student)
    else:
        print(' ')

        print('no student discount can be availled, fare:',discounted_price)
elif age>60:
    print(' ')
    
    print('senior citizen fare:',is_senior_citizen)
else:
    print(' ')

    print('no concession available, fare:',ticket_price)

print(' ')

print('thankyou, have a great journey')
    
        
