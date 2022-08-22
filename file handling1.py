#open for write and read

f=open('student.txt',mode='w+',encoding='utf-8')
print("file name",f.name)
print("file name",f.mode)
print("file name",f.readable())
print("file name",f.writable())
print("file name",f.closed)
f.close()
print("file close",f.closed)



#2.opening for reading

'''f=open('student.txt',mode='r',encoding='utf-8')
print("file name",f.name)
print("file name",f.mode)
print("file name",f.readable())
print("file name",f.writable())
print("file name",f.closed)
f.close()
print("file close",f.closed)'''


#3.open for binary read mode

'''f=open('student.txt',mode='rb')
print("file name",f.name)
print("file name",f.mode)
print("file name",f.readable())
print("file name",f.writable())
print("file name",f.closed)
f.close()
print("file close",f.closed)'''

#4.open text mode binary mode

'''f=open('student.txt',mode='w')
f.write('hello\n')
f.write('hiii\n')
f.write('how are u')
f.close()
print('writing success')

f=open('student.txt',mode='r')
data=f.read()
print(data)
f.close()

f=open('student.txt',mode='rb')
data=f.read()
print(data)
f.close()'''


#5.file object variables


'''f=open('student.txt',mode='r',encoding='utf-8')
print("file name",f.name)
print("file name",f.mode)
print("file name",f.readable())
print("file name",f.writable())
print("file name",f.closed)
f.close()
print("file close",f.closed)'''


#6.Append read mode

'''f=open('student.txt',mode='a+',encoding='utf-8')
print("file name",f.name)
print("file name",f.mode)
print("file name",f.readable())
print("file name",f.writable())
print("file name",f.closed)
f.close()
print("file close",f.closed)'''

#7.exclusive creation mode

'''f=open('student1.txt',mode='x',encoding='utf-8')
print("file name",f.name)
print("file name",f.mode)
print("file name",f.readable())
print("file name",f.writable())
print("file name",f.closed)
f.close()
print("file close",f.closed)'''


#8.read write mode

'''f=open('student.txt',mode='r+',encoding='utf-8')
print("file name",f.name)
print("file name",f.mode)
print("file name",f.readable())
print("file name",f.writable())
print("file name",f.closed)
f.close()
print("file close",f.closed)'''

#9.append mode
'''f=open('student.txt',mode='a',encoding='utf-8')
print("file name",f.name)
print("file name",f.mode)
print("file name",f.readable())
print("file name",f.writable())
print("file name",f.closed)
f.close()
print("file close",f.closed)'''

#10.binary exclusive creation mode

'''f=open('python.jpg',mode='xb')
print("file name",f.name)
print("file name",f.mode)
print("file name",f.readable())
print("file name",f.writable())
print("file name",f.closed)
f.close()
print("file close",f.closed)'''

#11.binary append mode

'''f=open('python3.jpg',mode='ab')
print("file name",f.name)
print("file name",f.mode)
print("file name",f.readable())
print("file name",f.writable())
print("file name",f.closed)
f.close()
print("file close",f.closed)'''


#12.binary read write mode

'''f=open('python1.jpg',mode='rb+')
print("file name",f.name)
print("file name",f.mode)
print("file name",f.readable())
print("file name",f.writable())
print("file name",f.closed)
f.close()
print("file close",f.closed)'''


#13.binart write mode
'''f=open('python1.jpg',mode='wb')
print("file name",f.name)
print("file name",f.mode)
print("file name",f.readable())
print("file name",f.writable())
print("file name",f.closed)
f.close()
print("file close",f.closed)'''


#14.binary write read mode
'''f=open('python.jpg',mode='wb+')
print("file name",f.name)
print("file name",f.mode)
print("file name",f.readable())
print("file name",f.writable())
print("file name",f.closed)
f.close()
print("file close",f.closed)'''

#15.binary append read mode
'''f=open('python.jpg',mode='rb+')
print("file name",f.name)
print("file name",f.mode)
print("file name",f.readable())
print("file name",f.writable())
print("file name",f.closed)
f.close()
print("file close",f.closed)'''

#16.file exists

'''import os
print(os.path.isfile('student.txt'))'''

#17.file exists2

'''import os
if os.path.isfile('student.txt'):
    f=open('student.txt')
    print('file opened')
    f.close()
else:
    print("file not found")'''


#18.write data with  a mode

'''f=open('student.txt',mode='a')
f.write('hello\n')
f.write('great.&\n')
f.write('how are u')
f.close()
print('success')'''


#19.write data2 with w mode

f=open('student.txt',mode='w')
f.write('hello\n')
f.write('great.&\n')
f.write('how are u')
f.close()
print('success')

#20.write data with x mode

'''f=open('student7.txt',mode='x')
f.write('hello\n')
f.write('great.&\n')
f.write('how are u')
f.close()
print('success')'''

#21.read data with r mode

'''f=open('student.txt',mode='r')
data=f.read()
print(data)
f.close()
print('completed!!')'''


#22.readlines method with r mode

'''f=open('student.txt',mode='r')
data=f.readlines()
print(data)
for i in data:
    print(i,end='')
f.close()'''

#23.reading data with r mode

'''f=open('student.txt',mode='r')
data1=f.read(2)
data2=f.read(2)
print(data1)
print(data2)
f.close()'''


#24.writelines method data with a mode

'''f=open('student.txt',mode='a')
lst=['rahul\n','sonam\n','sumit\n','rani\n','raj\n']
f.writelines(lst)
f.close()
print("success")'''


#25.writelines method data with w mode


'''f=open('student1.txt',mode='w')
lst=['rahul','sonam','sumit','rani']
f.writelines(lst)
f.close()
print('success')'''


#26.writing and then reading it will overwrite existing data

'''f=open('student.txt',mode='w+')
print(f.tell())
f.write('youtube')
print(f.tell())
f.seek(0)
print(f.tell())
data=f.read()
print(f.tell())
print(data)'''


#27.copy file content(copying content of one file to another file)

'''f1=open('student.txt',mode='r')
f2=open('student1.txt',mode='w')
data=f1.read()
f2.write(data)
print('success')'''


#28.seek method

'''f=open('student.txt',mode='r')
print(f.tell())
f.seek(7)
print(f.tell())
data1=f.read()
print(data1)
f.seek(2)
print(f.tell())
data2=f.read()
print(data2)'''


#29.tell method

'''f=open('student.txt',mode='r')
print(f.tell())
data1=f.read(5)
print(data1)
print(f.tell())
data2=f.read(3)
print(data2)
print(f.tell())'''











