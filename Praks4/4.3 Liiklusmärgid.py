from tkinter import *
 
raam = Tk()
raam.title("Märk")
tahvel = Canvas(raam, width=800, height = 400)

tahvel.create_rectangle(0, 110, 800, 270, fill="mediumblue", outline="mediumblue")

tahvel.create_rectangle(50, 230, 620, 150, fill="white", outline="white")

tahvel.create_polygon(617,115,617,263,790,190, fill="white",
outline="black")
 
 
tahvel.pack()
raam.mainloop()