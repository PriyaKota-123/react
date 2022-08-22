'''Write a Python GUI program to create  certain number of rows and columns of a Tkinter grid? and add differt color on each column
write a name,id,batch,feedback are columns 
each column has differnt color'''


from tkinter import *

root = Tk()
root.geometry("500x350")
root.config(bg="yellow")
frame = Frame(root)
frame.pack()
#bottomframe = Frame(root)
#label1 = Label(win, text='name', font=("Calibri, 15"))

#bottomframe.pack( side = BOTTOM )
button = Button(frame, text = 'name',bg='red',font =('Arial bold', 10))
button.grid(column=1, row=1)
#redbutton.pack( side = LEFT)
button = Button(frame, text = 'id', bg='pink',font=('Arial bold', 10))
button.grid(column=2, row=1)
button = Button(frame, text ='batch',bg='orange', font=('Arial bold', 10))
button.grid(column=3, row=1)
button = Button(frame, text ='feedback',bg='white',font=('Arial bold', 10))
button.grid(column=4, row=1)
root.mainloop()
