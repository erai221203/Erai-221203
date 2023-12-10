import from data management 


system = StudentManagementSystem()

system.add_student(input('enter your name:'), int(input('Enter your roll number:')), int(input('marks:')))
system.add_student(input('enter your name:'), int(input('Enter your roll number:')), int(input('marks:')))
system.add_student(input('enter your name:'), int(input('Enter your roll number:')), int(input('marks:')))
system.get_student_details(1)
system.get_student_details(2)
system.get_student_details(3)

system.remove_student(2)

system.display_all_students()

