from tkinter import *
from tkinter import messagebox

root = Tk()
scale = [500,400]

root.config(background= "red")
root.iconbitmap("images.ico")
root.resizable(0,0)
root.title("Edaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaad")

frm = Frame(root, width= scale[0], height= scale[1], background="blue")
frm.pack()

text_text = "Ingresa tu edad en la siguiente entrada:"

scale_B = [1, 1]
pos_B = [scale[0]/2 - scale_B[0], scale[1]/2 - scale_B[1]]

text = Label(frm, text= text_text)
text.place(x= scale[0]/2 - 100, y = scale[1]/2 - 50)

def only_numbers(char):
   return char.isdigit()
validation = root.register(only_numbers)

ent = Entry(frm, validate="key", validatecommand=(validation, '%S'))
ent.place (x= scale[0]/2 - 55, y = scale[1]/2 - 20)

def helloCallBack(entry = Entry):

   val = entry.get().isdigit()

   if entry.get() == "":
      msg = messagebox.showerror( "Error", "No has ingresado tu edad \n \n Porfavor, ingresa tu edad")
   else:
      if int(entry.get()) <= 0:
         msg = messagebox.showinfo( "Tu edad", "No tienes ni un año xd")
      if int(entry.get()) == 1:
         msg = messagebox.showinfo( "Tu edad", "Tienes: " + "1" + " año de edad")
      else:
         msg = messagebox.showinfo( "Tu edad", "Tienes: " + entry.get() + " años de edad")



B = Button(frm, text = "Calcular")
B.config(command= lambda: helloCallBack(entry= ent))
B.place(x= scale[0]/2 - 20, y = scale[1]/2 + 40)

root.mainloop()