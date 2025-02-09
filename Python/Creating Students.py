# Creating students filee
students = open("D:\\ZagEng 2025\\AI-Track\\Python\\students.txt", "w")
students.write("Student Name,Subject,Degree\n")
students.write("Tasnim,English,45\n")
students.write("Tahany,Arabic,95\n")
students.write("Menna,Math,75\n")
students.write("Basmala,History,85\n")
students.write("Aml,English,65\n")
students.write("Malak,Math,61\n")
students.write("Mariam,Programming,61\n")
students.close()

# load students Data 
def loadStudents():
    studentslist = []
    students =  open("D:\\ZagEng 2025\\AI-Track\\Python\\students.txt", "r") 
    lines = students.readlines()
    for line in lines[1:]:  
        name, subject, degree = line.strip().split(',')
        studentslist.append({"Name": name.strip(), "Subject": subject.strip(), "Degree": int(degree)})
    return studentslist

# Check student data
def validStudent(name, subject, students):
    name = name.lower()
    subject = subject.lower()
    for student in students:
        if student["Name"].lower() == name and student["Subject"].lower() == subject:
            return True
    return False

# add new student to file 
def addStudent(name, subject, degree):
    students =  open("D:\\ZagEng 2025\\AI-Track\\Python\\students.txt", "a") 
    students.write(f"{name},{subject},{degree}\n")

# load existing students
students = loadStudents()


print("Hi! This is a student management system to help you. In case you want to leave, enter Exit.")

while True:
    choice = input("Do you want to add a new student or view grades? (view/add): ").lower()
    if choice == "exit":
        break

    if choice == "view":
        name = input("Enter student name: ")
        subject = input("Enter subject: ")
        if validStudent(name, subject, students):
            
            degree = next(
                (s["Degree"] for s in students if s["Name"].lower() == name.lower() and s["Subject"].lower() == subject.lower()),
                None
            )
            print(f"Student {name} has a degree of {degree} in {subject}.")
        else:
            print("Invalid student or subject. Please try again.")

    elif choice == "add":
        name = input("Enter new student name: ")
        subject = input("Enter subject: ")
        while True:
            degree = input("Enter degree: ")
            if degree.isdigit() and 0 <= int(degree) <= 100:
                degree = int(degree)
                break
            else:
                print("Degree must be a number between 0 and 100.")
        addStudent(name, subject, degree)
        students.append({"Name": name, "Subject": subject, "Degree": degree})
        print("Student added successfully.")

    else:
        print("Invalid choice. Please enter 'view' or 'add'.")
