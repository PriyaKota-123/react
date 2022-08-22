##Problem Statement: Write a program to build a simple Student Management System using Python which can perform the following operations in oops concepts 
##1.Accept
##2.Display
##3.Search
##4.Delete
##5.Update


class Student():
    def __init__(self,student_name,roll_no,marks,percentage):
        self.student_name=student_name
        self.roll_no=roll_no
        self.marks=marks
        self.percentage=percentage

    def accept(self,student_name,roll_no,marks,percentage):
        a = Student(student_name,roll_no,marks,percentage)
        ls.append(a)
    def display(self, a):
        print("Name : ", a.student_name)
        print("RollNo : ", a.roll_no)
        print("Marks1 : ", a.marks)
        print("Marks2 : ", a.percentage)
        print("\n")

    def search(self, rn):
        for i in range(ls.__len__()):
            if(ls[i].roll_no == rn):
                return i
    def delete(self, rn):
        i = b.search(rn)
        del ls[i]
    def update(self, rn, No):
        i = b.search(rn)
        roll = No
        ls[i].roll_no = roll

ls = []
b = Student('',0,0,0)
b.accept("vicky", 1, 100, 89)
b.accept("picky", 2, 90, 60)
b.accept("picklu", 3, 80, 80)

for i in range(ls.__len__()):
    b.display(ls[i])

print("\n Student Found, ")
s = b.search(2)
b.display(ls[s])

b.delete(2)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):
    b.display(ls[i])

b.update(3, 2)
print(ls.__len__())
print("List after updation")
for i in range(ls.__len__()):
    b.display(ls[i])

print("Thank You !")
