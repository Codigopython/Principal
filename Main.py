from tkinter import *
from Modulos import *
#frame principal
gui = Tk()
gui.title('Calculadora')
gui.geometry('240x325+1000+100')
gui.config(bg='white')

#Cajas de operaciones
lista1 = Listbox(relief=SUNKEN,bd=0,height=3,width=17,font=("Ubuntu",15))
lista2 = Listbox(bd=0,height=1,width=17,font=("Ubuntu",15))
caja1 = Entry(bd=0,width=17,font=("ubuntu",15))


lista1.pack()
lista2.pack()
caja1.pack()

#botones del 0 al 9
boton1 = Button(bd=0, text='7', font=('ubuntu',24),
command=lambda: caja1.insert(END,'7'))
boton1.place(height=40, width=40,x=10,y=140)

boton1 = Button(bd=0, text='8', font=('ubuntu',24),
command=lambda: caja1.insert(END,'8'))
boton1.place(height=40, width=40,x=55,y=140)

boton1 = Button(bd=0, text='9', font=('ubuntu',24),
command=lambda: caja1.insert(END,'9'))
boton1.place(height=40, width=40,x=100,y=140)

boton1 = Button(bd=0, text='4', font=('ubuntu',24),
command=lambda: caja1.insert(END,'4'))
boton1.place(height=40, width=40,x=10,y=185)

boton1 = Button(bd=0, text='5', font=('ubuntu',24),
command=lambda: caja1.insert(END,'5'))
boton1.place(height=40, width=40,x=55,y=185)

boton1 = Button(bd=0, text='6', font=('ubuntu',24),
command=lambda: caja1.insert(END,'6'))
boton1.place(height=40, width=40,x=100,y=185)

boton1 = Button(bd=0, text='3', font=('ubuntu',24),
command=lambda: caja1.insert(END,'3'))
boton1.place(height=40, width=40,x=100,y=230)

boton1 = Button(bd=0, text='2', font=('ubuntu',24),
command=lambda: caja1.insert(END,'2'))
boton1.place(height=40, width=40,x=55,y=230)

boton1 = Button(bd=0, text='1', font=('ubuntu',24),
command=lambda: caja1.insert(END,'1'))
boton1.place(height=40, width=40,x=10,y=230)

boton1 = Button(bd=0, text='0', font=('ubuntu',24),
command=lambda: caja1.insert(END,'0'))
boton1.place(height=40, width=40,x=10,y=275)

#Botones de operaciones matematicas
boton1 = Button(bd=0, text='+', font=('ubuntu',24),
command=lambda:(lista2.insert(0,Suma(caja1.get())),
lista1.insert(0,caja1.get()),caja1.delete(0,END)))
boton1.place(height=85, width=40,x=145,y=230)

boton1 = Button(bd=0, text='-', font=('ubuntu',24),
command=lambda:(lista2.insert(0,Resta(caja1.get())),
lista1.insert(0,caja1.get()),caja1.delete(0,END)))
boton1.place(height=85, width=40,x=145,y=140)

boton1 = Button(bd=0, text='x', font=('ubuntu',24),
command=lambda:(lista2.insert(0,Multi(caja1.get())),
lista1.insert(0,caja1.get()),caja1.delete(0,END)))
boton1.place(height=85, width=40,x=190,y=140)

boton1 = Button(bd=0, text='/', font=('ubuntu',24),
command=lambda:(lista2.insert(0,Divi(caja1.get())),
lista1.insert(0,caja1.get()),caja1.delete(0,END)))
boton1.place(height=85, width=40,x=190,y=230)

#Boton igual
boton1 = Button(bd=0, text='=', font=('ubuntu',24),
command=lambda:(lista2.insert(0,Igual(caja1.get())),
lista1.insert(0,caja1.get()),caja1.delete(0,END)))
boton1.place(height=40, width=40,x=55,y=275)

#Boton Clear
boton1 = Button(bd=0, text='CE', font=('ubuntu',20),
command=lambda:(Clear(),lista1.delete(0,END),lista2.delete(0,END)))
boton1.place(height=40, width=40,x=100,y=275)

gui.mainloop()
