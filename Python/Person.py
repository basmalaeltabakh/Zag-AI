class Student:
    def __init__(self,name, id ):
        self.name=name
        self.id=id
        self.cources = []
    def enroll(self,cource) :
        self.cources.append(cource)
        print (f"{self.name} enrolled in cources")
    def display(self):
        print (f"Student : {self.name} , ID : {self.id} , Cources : {', '. join(self.cources)}")
s1 = Student("Basmala" , 555555)
s2= Student("Tasnim",222222)
s3=Student("Tahany" , 44444)
s1.enroll(" Programming 2 ")
s1.display()
s2.enroll("Math 3")
s2.display()
s3.enroll("OS")
s3.display()