def exception(a,b):
        try :
            result=a/b
            print(result)
        except ZeroDivisionError:
            print('Error')
exception(10,0)

def ex(a):
    try:
        if type(a)!=int:
                print(a,'is not a valid integer')
        
    except ValueError:
         print(a,'is a valid integer')
    
                    
ex(10)