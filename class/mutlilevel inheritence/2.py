
#multilevel inheritence 

'''class Employees(): 
 
   def Name(self): 
       print("Employee Name: Khush")
 
class salary(Employees):
   def Salary(self):
       print("Salary: 10000")
 
class Designation(salary):
   def desig(self):
       print("Designation: Test Engineer")
 
call = Designation()
call.Name()
call.Salary()
call.desig()'''


class Employees():
    def __init__(self,age,id):
        self.age=age
        self.id=id
 
    def Name(self): 
       print("Employee Name: Khush")
 
class salary(Employees):
    def __init__(self,age,id):
        super().__init__(age,id)
    def Salary(self):
       print("Salary: 10000")
       print("age:22")
       print("id:2")
 
class Designation(salary):
    def __init__(self,age,id):
        super().__init__(age,id)
    def desig(self):
       print("Designation: Test Engineer")
 
call = Designation(22,19)
call.Name()
call.Salary()
call.desig()
call.age()
call.id()




