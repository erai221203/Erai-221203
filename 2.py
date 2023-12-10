class Student:
    def __init__(self, roll_number, name, age, grade):
        self.roll_number = roll_number
        self.name = name
        self.age = age
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("Student added successfully!")

    def display_students(self):
        print("Student List:")
        for student in self.students:
            print(f"Roll Number: {student.roll_number}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
    
    def find_student(self, roll_number):
        return next((student for student in self.students if student.roll_number == roll_number), None)
    
    def delete_student(self, roll_number):
        student = self.find_student(roll_number)
        if student:
            self.students.remove(student)
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    def update_student(self, roll_number, new_name, new_age, new_grade):
        student = self.find_student(roll_number)
        if student:
            student.name, student.age, student.grade = new_name, new_age, new_grade
            print("Student information updated successfully!")
        else:
            print("Student not found.")

sms = StudentManagementSystem()

while True:
    print("\nStudent Management System Menu:")
    print("1. Add Student\n2. Display Students\n3. Search Student\n4. Delete Student\n5. Update Student\n6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        sms.add_student(Student(input("Roll Number: "), input("Name: "), int(input("Age: ")), input("Grade: ")))
    elif choice == "2":
        sms.display_students()
    elif choice == "3":
        roll_number = input("Enter Roll Number to search: ")
        student = sms.find_student(roll_number)
        print(f"Student found - Name: {student.name}, Age: {student.age}, Grade: {student.grade}") if student else print("Student not found.")
    elif choice == "4":
        sms.delete_student(input("Enter Roll Number to delete: "))
    elif choice == "5":
        roll_number = input("Enter Roll Number to update: ")
        sms.update_student(roll_number, input("New Name: "), int(input("New Age: ")), input("New Grade: "))
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
