from tkinter import * 
import sys
import time 

master = Tk()
master.title("Digitale Uhr")

def get_time():
    timeVar = time.strftime("%H:%M:%S")
    uhr.config(text=timeVar)
    uhr.after(200,get_time)
                
uhr=Label(master, font=("Calibri",150),bg="black",fg="blue")
uhr.pack()           
get_time()
master.mainloop()


