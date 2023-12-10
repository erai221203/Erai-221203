'''Write and execute a python function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20'''

l=int(input('Enter any value:'))
s = 0
for i in range(l + 1):
    if i % 3 == 0 or i % 5 == 0:
        s += i
        print(i)
print('Sum of the given limit of',l,'is',s)
