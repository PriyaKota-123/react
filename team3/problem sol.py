##Write a Python class named Student with two instances student1, student2 and assign given values to the said instances attributes.
##Print all the attributes of student1, student2 instances with their values in the given format.
##
##Input values of the instances:
##student_1:
##student_id = "V12"
##student_name = "Ernesto Mendez"
##student_2:
##student_id = "V12"
##marks_language = 85
##marks_science = 93
##marks_math = 95
##Expected Output:
##student_id -> V12
##student_name -> Ernesto Mendez
##student_id -> V12
##marks_language -> 85
##marks_science -> 93
##marks_math -> 95

class student:
    def __init__(self):
        self.id=int(input("Enter any id number="))
        self.name=input("Enter  student name=")
        self.marks_language=int(input("Enter telugu marks="))
        self.marks_science=int(input("Enter science marks="))
        self.marks_math=int(input("Enter math marks="))
    def student1(self):
        print("student id={}".format(self.id))
        print("student name={}".format(self.name))
    def student2(self):
        print("marks_telugu={}".format(self.marks_language))
        print("marks_science={}".format(self.marks_science))
        print("marks_math={}".format(self.marks_math))

result=student()
result.student1()
result.student2()
