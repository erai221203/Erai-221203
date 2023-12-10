class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        
class StudentManagementSystem:
    def __init__(self):
        self.students = []
        
    def add_student(self, name, roll_no, marks):
        student = Student(name, roll_no, marks)
        self.students.append(student)
        
    def remove_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print(f"Student with roll no. {roll_no} removed.")
                return
        print(f"Student with roll no. {roll_no} not found.")
        
    def get_student_details(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print(f"Name: {student.name}")
                print(f"Roll No.: {student.roll_no}")
                print(f"Marks: {student.marks}")
                return
        print(f"Student with roll no. {roll_no} not found.")
        
    def display_all_students(self):
        for student in self.students:
            print(f"Name: {student.name}")
            print(f"Roll No.: {student.roll_no}")
            print(f"Marks: {student.marks}")
            print()

system = StudentManagementSystem()

system.add_student(input('enter your name:'), int(input('Enter your roll number:')), int(input('marks:')))
system.add_student(input('enter your name:'), int(input('Enter your roll number:')), int(input('marks:')))
system.add_student(input('enter your name:'), int(input('Enter your roll number:')), int(input('marks:')))
system.get_student_details(1)
system.get_student_details(2)
system.get_student_details(3)

system.remove_student(2)

system.display_all_students()

