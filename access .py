
class cls:
    def public_method(self):
        print("This is a public method.")
    def _protected_method(self):
        print("This is a protected method.")
    def __private_method(self):
        print("This is a private method.")
obj = cls()
obj._protected_method()
obj.public_method()
obj._cls__private_method()
'''
print(obj.public_var)
obj.public_method()
print(obj._protected_var)
obj._protected_method()
print(obj._MyClass__private_var)
obj._MyClass__private_method()'''