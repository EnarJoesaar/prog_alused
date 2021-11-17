from tkinter import *
 
raam = Tk()
raam.title("Kalmaari maja")
tahvel = Canvas(raam, width=1000, height = 600)
# tee
tahvel.create_rectangle(0, 0, 1000, 1000, fill="slategrey", outline="slategrey")
# liiv
tahvel.create_rectangle(0, 0, 1000, 550, fill="bisque", outline="bisque")
# maja struktuur
tahvel.create_rectangle(400, 70, 600, 500, fill="dimgray", outline="dimgray")
#uks
tahvel.create_rectangle(470, 390, 530, 500, fill="peru", outline="peru")
tahvel.create_oval(470,380,530,400, fill="peru", outline="peru")
#nina
tahvel.create_rectangle(468, 370, 530, 205, fill="dimgray", outline="black")
#silmad/aknad
tahvel.create_oval(405,270,465,210, fill="blue", outline="blue")
tahvel.create_oval(533,270,595,210, fill="blue", outline="blue")
#kulmud
tahvel.create_rectangle(420, 200, 580, 150, fill="dimgray", outline="black")
#Kõrvad
tahvel.create_rectangle(340, 370, 400, 205, fill="dimgray", outline="black")
tahvel.create_rectangle(600, 370, 660, 205, fill="dimgray", outline="black")
#maja esine tee
tahvel.create_rectangle(468, 540, 530, 547, fill="dimgray", outline="black")
tahvel.create_rectangle(468, 530, 530, 537, fill="dimgray", outline="black")
tahvel.create_rectangle(468, 520, 530, 527, fill="dimgray", outline="black")
tahvel.create_rectangle(468, 510, 530, 517, fill="dimgray", outline="black")

 
tahvel.pack()
raam.mainloop()