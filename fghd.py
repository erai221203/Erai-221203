a=input('enter:')

def palindrome(str):
    str=str.lower().replace(' ',' ')
    return str==str[::-1]
print(palindrome(a))
