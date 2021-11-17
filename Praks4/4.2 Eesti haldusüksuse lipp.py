from tkinter import *
 
raam = Tk()
raam.title("Lipp")
tahvel = Canvas(raam, width=880, height = 600)
 
tahvel.create_rectangle(0, 0, 880, 300, fill="blue", outline="blue")
 
tahvel.create_rectangle(0, 200, 880, 400, fill="black", outline="black")

tahvel.create_rectangle(0, 400, 880, 600, fill="yellow", outline="yellow")
 
tahvel.pack()
raam.mainloop()