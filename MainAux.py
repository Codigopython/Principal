from tkinter import *
from ModulosAux import *

gui = Tk()

lista1 = Listbox()
caja1 = Entry()

boton1 = Button(text="+",font=("ubuntu",20),
command=lambda:Suma(caja1.get()))

boton2 = Button(text="-",font=("ubuntu",20),
command=lambda:Resta(caja1.get()))


boton3 = Button(text="clear",font=("ubuntu",20),
command=lambda:a)


lista1.pack()
caja1.pack()
boton1.pack()
boton2.pack()
boton3.pack()

gui.mainloop()
