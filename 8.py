#8.Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical. 
def excep(self):
    try:
        a=int(input('Enter any value:'))
        b=int(input('Enter any value:'))
    
        c=a+b
        print(c)
    except ValueError:
        print(' the values in not an integer')

excep(0)