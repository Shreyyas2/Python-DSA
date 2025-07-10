year=int(input('enter a year:'))
if year%2==0:
    print('the entered year is even')
    if year/4:
        print('the entered year is an leap year')
    else:
        print('the entered year is not an leap year')
else:
    print('the entered year is odd')
