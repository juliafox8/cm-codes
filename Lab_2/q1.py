import tkinter
from tkinter import Canvas 

def olympic_rings():
    window = tkinter.Tk()
    c = Canvas(window, width = 600, height = 400)
    
    #blue
    c.create_oval(10, 10, 50, 50, fill= "blue")
    c.create_oval(15, 15, 45, 45, fill = "white")

    #black
    c.create_oval(50, 10, 90, 50, fill = "black")
    c.create_oval(55, 15, 85, 45, fill = "white")

    #red
    c.create_oval(90, 10, 130, 50, fill = "red", outline= "black")
    c.create_oval(95, 15, 125, 45, fill = "white",outline= "black" )
   
    #yellow
    c.create_oval(30, 45, 70, 85, fill = "yellow")
    c.create_oval(35, 50, 65, 80, fill = "white")
    
    #green
    c.create_oval(70, 45, 110, 85, fill = "green")
    c.create_oval(75, 50, 105, 80, fill = "white")
   
    c.pack()
    window.mainloop()

olympic_rings()