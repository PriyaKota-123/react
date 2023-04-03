#digital watch
import sys
from tkinter import *
import time
 
def timing():
    
    current_time = time.strftime("%H : %M : %S")
    
    clock.config(text=current_time)
    
    clock.after(200,timing)
 

root=Tk()

root.geometry("500x200")
clock=Label(root,font=("times",60,"bold"))
clock.grid(row=2,column=2,pady=25,padx=100)
timing()
root.mainloop()
