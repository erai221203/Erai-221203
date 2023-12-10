print('\H ******Rules*******')

a=int(input('Enter your age:'))
g=input('Enter your gender:')
m=input('Are you married or not:')

if g=='M':
    if a>20 and a<40 :
        print('YOU CAN WORK ANYWHERE')
    elif a>40 and a<60:
        print('YOU CAN ONLY WORK IN URBAN AREAS')
    else:
        print('Error')
        
elif g=='F' and m=='Y':
    print('YOU CAN ONLY WORK IN URBAN AREAS')
else:
    print('SORRY,ENTER CORRECTLY')
