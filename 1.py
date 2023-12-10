#Write a Program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object
class Students:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
s1=Students('Erai',19,'1st year')
s2=Students('Anbu',15,'1st')
print(s1.name)
print(s1.age)