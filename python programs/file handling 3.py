##24.Consider a binary file “data.dat” which stores the record of “Hotel” in the form of list containing Room_no, Price, Room_type. Do the following task in a file 
##
##1.Write a function addrec() to add a record in a file.

'''import pickle
def addrec():
     L=[ ]
     f=open("data.dat","ab")
     rn = int(input("Enter Room Number"))
     pr = int(input("Enter the price of room"))
     rt = input("Enter the type of room")
     L  = [rn, pr, rt]
     pickle.dump(L, f)
     print("Record added in the file")
     f.close()
addrec()'''
##2.Write a function disp() to display all the records from the file.

'''import pickle
def disp():
  try:
      f=open("data.dat","rb")
      while True:
            d=pickle.load(f)
            print(d)
  except:
      f.close()
disp()'''

##3.Write a function specific_disp(room_no) which takes room number as argument and display its details.

'''import pickle
def specific_rec(rno):
  try:
    f1=open("data.dat","rb")
    while True:
      d=pickle.load(f1)
      if rno==d[0]:
          print(d)
  except:
    f1.close()
    
rno=int(input("Enter Room number to search"))
specific_rec(rno)
'''
##4.Write a function mod(room_no) which takes room number as argument and modify it’s details.

'''import pickle
import os
def mod():
  roll = int(input("Enter room number whose record you want to Modify:"))
  
  try:
      file = open("data.dat","rb+")
      f=open("temp1.dat","wb")
      
      while True:
          d = pickle.load(file)
          if roll == d[0]:
              d[1]=int(input("Enter modified price"))
              d[2]=input("Enter modified room type")
          pickle.dump(d,f)
  except:
      print("Record Updated")
      file.close()
      f.close()
      os.remove("data.dat")
      os.rename("temp1.dat","data.dat")
mod()
 '''
##5.Write a function del(room_no) which takes room number as argument and delete it’s record from file “data.dat”


'''import pickle
import os
def delete():
  roll = int(input("Enter room number whose record you want to delete:"))
  try:
      file = open("data.dat","rb+")
      f=open("temp1.dat","wb")
      while True:
          d = pickle.load(file)
          if roll != d[0]:
              pickle.dump(d,f)
          else:
              found = 1
      
  except:
      print("Record Deleted")
      file.close()
      f.close()
      os.remove("data.dat")
      os.rename("temp1.dat","data.dat")
delete()'''

##25.Write a menu driven program which shows all operations on Binary File 
##
##Add Record 
'''import pickle
import os
def main_menu():
    print("1. Add a new record")
    print("2. Display all record")
    print("3. Display Specific record")
    print("4. Modify a record")
    print("5. Delete a record")
    print("6. Exit")
    ch = int(input("Enter your choice:"))
    if ch==1:
        addrec()
    elif ch==2:
        disp()
    elif ch==3:
        
        specific_rec()
    elif ch==4:
        mod()
    elif ch==5:
        del()
    elif ch==6:
        print("Bye")
    else:
        print("Invalid Choice.")'''
##Display All Record 
'''def addrec():
     L=[ ]
     f=open("data.dat","ab")
     rn = int(input("Enter Room Number"))
     pr = int(input("Enter the price of room"))
     rt = input("Enter the type of room")
     L  = [rn, pr, rt]
     pickle.dump(L, f)
     print("Record added in the file")
     f.close()'''
##Display Specific Record

'''def disp():
  try:
      f=open("data.dat","rb")
      while True:
            d=pickle.load(f)
            print(d)
  except:
      f.close()

def specific_rec():
  rno=int(input("Enter Room number to search"))
  try:
    f1=open("data.dat","rb")
    while True:
      d=pickle.load(f1)
      if rno==d[0]:
          print(d)
  except:
    f1.close()'''
##
##Modify Record
'''def mod():
  roll = int(input("Enter room number whose record you want to Modify:"))
  try:
      file = open("data.dat","rb+")
      f=open("temp1.dat","wb")
      
      while True:
          d = pickle.load(file)
          if roll == d[0]:
              d[1]=int(input("Enter modified price"))
              d[2]=input("Enter modified room type")
          pickle.dump(d,f)
 except:
      print("Record Updated")
      file.close()
      f.close()
      os.remove("data.dat")
      os.rename("temp1.dat","data.dat")
'''
##Delete Record

'''def delete():
  roll = int(input("Enter room number whose record you want to delete:"))
  try:
      file = open("data.dat","rb+")
      f=open("temp1.dat","wb")
      while True:
          d = pickle.load(file)
          if roll != d[0]:
              pickle.dump(d,f)
  except:
      print("Record Deleted")
      file.close()
      f.close()
      os.remove("data.dat")
      os.rename("temp1.dat","data.dat")'''

##Use “data.dat” file which stores the record of “Hotel” in the form of list containing Room_no, Price, Room_type



##
##26.Write a function disp75() in Python to display only those records of students from file “school.dat” who scored more than 75 percent marks. Structure stored in “school.dat” is in the form of list containing information like [rollno, name, class, percentage] 
'''def disp75():
  f=open("studen.txt", "rb")
  try:
    while True:
      d=pickle.load(f)
      if d[3]>75:
        print("Roll Number : ", d[0], "\n")
        print("Name            : ", d[1], "\n")
        print("Class             : ", d[2], "\n")
        print("Percentage   : ", d[3], "\n")
  except:
    f.close()
disp75()'''



##27.Write a function dispname() in Python which will display only names of all the students from file “school.dat”. Structure stored in “school.dat” is in the form of list containing information like [rollno, name, class, percentage] 
'''def dispname():
  f=open("studen.txt","rb")
  try:
    while True:
      d=pickle.load(f)
      print("Name        : ", d[1],"\n")
  except:
    f.close()
dispname()'''

##28.Write a function disp12() in Python which will display records of class 12th students from file “school.dat”. Structure stored in “school.dat” is in the form of list containing information like [rollno, name, class, percentage] 
'''def disp12( ):
  f=open("studen.txt", "rb")
  try:
    while True:
      d=pickle.load(f)
      if int(d[2]) == 12:
        print("Roll Number : ", d[0],"\n")
        print("Name           : ", d[1],"\n")
        print("Class            : ", d[2],"\n")
        print("Percentage  : ", d[3],"\n")
  except:
    f.close( )
disp12( )'''
##29.Write a function search(name) in Python which will display record of a student from file “school.dat” whose name is passed as an argument. Structure stored in “school.dat” is in the form of list containing information like [rollno, name, class, percentage] 
'''def search(nm):
  f=open("studen.txt","rb")
  try:
    while True:
      d=pickle.load(f)
      if d[1].lower() == nm.lower():
        print("Roll Number : ", d[0],"\n")
        print("Name           : ", d[1],"\n")
        print("Class            : ", d[2],"\n")
        print("Percentage  : ", d[3],"\n")
  except:
    f.close()
nm=input("Enter name of the student")
search(nm)'''
##30.Write a function disp_mob(model no.) in Python which will display the record of a mobile from “mobile.dat” whose model number (integer type) is passed as an argument. Structure of “mobile.dat” is [Mobile id, Mobile brand, Model No., Price

'''import pickle
import os
def rem():
     f=open("studen.txt", "rb")
     f1=open("data.txt", "wb")
     try:
        while True:
            d=pickle.load(f)
            if(d[3])>30:
                 pickle.dump(d, f1)     
     except:
        f.close()
        f1.close()
        os.remove("studen.txt")
        os.rename("data.txt", "studen.dat")
rem()'''
