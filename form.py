print("Welcome to the KCT College Application Form")

# get the student's personal information
name = input("Full Name: ")
email = input("Email Address: ")
phone = input("Phone Number: ")
address = input("Address: ")

# get the student's academic information
marks_10th = input("10th Marks: ")
marks_12th = input("12th Marks: ")
marks_grad = input("Graduation Marks: ")

# get the student's preferred course
course = input("Preferred Course: ")

# print the completed form
print("\n\n---KCT College Application Form---\n\n")
print("Full Name: " + name)
print("Email Address: " + email)
print("Phone Number: " + phone)
print("Address: " + address)
print("10th Marks: " + marks_10th)
print("12th Marks: " + marks_12th)
print("Graduation Marks: " + marks_grad)
print("Preferred Course: " + course)

# save the form to a file
file_name = name.lower().replace(" ", "_") + "_application_form.txt"
with open(file_name, "w") as f:
    f.write("---KCT College Application Form---\n\n")
    f.write("Full Name: " + name + "\n")
    f.write("Email Address: " + email + "\n")
    f.write("Phone Number: " + phone + "\n")
    f.write("Address: " + address + "\n")
    f.write("10th Marks: " + marks_10th + "\n")
    f.write("12th Marks: " + marks_12th + "\n")
    f.write("Graduation Marks: " + marks_grad + "\n")
    f.write("Preferred Course: " + course + "\n")
print("Your form has been saved to " + file_name)
