# multilevel inheritance
class grandma:
 
	def __init__(self, grandmaname):
		self.grandmaname = grandmaname
	def g(self):
            print("grandma name is")
class mother(grandma):
	def __init__(self, mothername, grandmaname):
		self.mothername = mothername
	def m(self):
            print("mother name is")
            grandma.__init__(self, grandmaname)
 

class son(mother):
	def __init__(self,sonname, mothername, grandmaname):
		self.sonname = sonname
	def s(self):
            print("grandma name is")
 
		# invoke a constructor of mother class
	father.__init__(self, mothername, grandmaname)
 
c=son("priya","purna","vicky")
c.g()
c.m()
c.s()
