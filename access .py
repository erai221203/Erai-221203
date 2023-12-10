class MyClass:
    def __init__(self):
        self.public_var = 10
        self._protected_var = 20
        self.__private_var = 30
    def public_method(self):
        print("This is a public method.")
    def _protected_method(self):
        print("This is a protected method.")
    def __private_method(self):
        print("This is a private method.")
obj = MyClass()
print(obj.public_var)
obj.public_method()
print(obj._protected_var)
obj._protected_method()
print(obj._MyClass__private_var)
obj._MyClass__private_method()