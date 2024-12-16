Students = []
def ValidName(name):
    return name.isalpha()
def CalcGrade(grade):
    if 90 <= grade <= 100:
        return 'A'
    elif 80 <= grade < 90:
        return 'B'
    elif 70 <= grade < 80:
        return 'C'
    elif 60 <= grade < 70:
        return 'D'
    else:
        return 'F'
def Display():
    print("\t\t\t Student Grade Management System \n")
    counter = 1
    for Student in Students:
        print(f"{counter}. Name: {Student['Name']} | Subject: {Student['Subject']} | Marks: {Student['Marks']} | Grade: {Student['Grade']}")
        counter += 1
while True:
    print("\nEnter Student Details:  \n")

    while True:
        name = input("Enter Student Name: ")
        if ValidName(name):
            break
        else:
            print("Invalid name! Please enter letters only.")

    subject = input("Enter Subject: ")


    while True:
        marks = input("Enter Marks (0-100): ")
        if marks.isdigit() and 0 <= int(marks) <= 100:
            marks = int(marks)
            break
        else:
            print("Marks must be a number between 0 and 100!")

    grade = CalcGrade(marks)


    student_data = {"Name": name, "Subject": subject, "Marks": marks, "Grade": grade}
    Students.append(student_data)

    AddStudent = input("Do you want to add another student? (yes/no): ").lower()
    if AddStudent != 'yes':
        break

Display()