#9.Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical. 
def excep(self):
    try:
        a=(input('Enter any value:'))
        b=input('Enter any value:')
        c=a*b
        print(c)
    except TypeError:
        print(' the values in not an integer')

excep(0)