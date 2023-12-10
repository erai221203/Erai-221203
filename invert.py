#Write and execute a python Program to read a number and print an inverted star pattern of the desired size 

n = int(input("Enter the size of the inverted triangle pattern: "))

for i in range(n, 0, -1):
    for j in range(n-i):
        print(' ', end=' ')
    for j in range(0, 2*i-1):
        print('*', end=' ')
    print()


