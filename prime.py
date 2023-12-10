n=int(input('Enter any number:'))

if n==2:
    print('prime')
elif  n < 2:
    print('no')
for i in range(2, int(n * 0.5) + 1):
    if n % i == 0:
        print('not a prime')
    else:
        print('prime')

'''# Python program to check if a number is prime or not using only if-else

num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
        
# if input number is less than or equal to 1, it is not prime
else:
    print(num, "is not a prime number")'''



    


