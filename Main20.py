#version 1.0
#by kelvin romani ollero
from tkinter import *
from Modulos20 import *

#frame principal
gui = Tk()
gui.title('Calculadora')
gui.geometry('240x325+1000+100')
gui.config(bg='white')

#Cajas de operaciones
lista1 = Listbox(relief=SUNKEN,bd=0,height=3,width=24,font=("Ubuntu",13))
lista2 = Listbox(bd=0,height=1,width=17,font=("Ubuntu",17))
caja1 = Entry(bd=0,width=17,font=("ubuntu",17))

lista1.pack()
lista2.pack()
caja1.pack()

#botones del 0 al 9
boton7 = Button(bd=0, text='7', font=('ubuntu',24),
command=lambda: caja1.insert(END,'7'))
boton8 = Button(bd=0, text='8', font=('ubuntu',24),
command=lambda: caja1.insert(END,'8'))
boton9 = Button(bd=0, text='9', font=('ubuntu',24),
command=lambda: caja1.insert(END,'9'))
boton4 = Button(bd=0, text='4', font=('ubuntu',24),
command=lambda: caja1.insert(END,'4'))
boton5 = Button(bd=0, text='5', font=('ubuntu',24),
command=lambda: caja1.insert(END,'5'))
boton6 = Button(bd=0, text='6', font=('ubuntu',24),
command=lambda: caja1.insert(END,'6'))
boton3 = Button(bd=0, text='3', font=('ubuntu',24),
command=lambda: caja1.insert(END,'3'))
boton2 = Button(bd=0, text='2', font=('ubuntu',24),
command=lambda: caja1.insert(END,'2'))
boton1 = Button(bd=0, text='1', font=('ubuntu',24),
command=lambda: caja1.insert(END,'1'))
boton0 = Button(bd=0, text='0', font=('ubuntu',24),
command=lambda: caja1.insert(END,'0'))

#Botones de operaciones matematicas
botonS = Button(bd=0, text='+', font=('ubuntu',24),
command=lambda:(lista2.insert(0,Operacion(caja1.get(),"su")),
lista1.insert(0,caja1.get()),caja1.delete(0,END)))

botonR = Button(bd=0, text='-', font=('ubuntu',24),
command=lambda:(lista2.insert(0,Operacion(caja1.get(),"re")),
lista1.insert(0,caja1.get()),caja1.delete(0,END)))

botonP = Button(bd=0, text='x', font=('ubuntu',24),
command=lambda:(lista2.insert(0,Operacion(caja1.get(),"mu")),
lista1.insert(0,caja1.get()),caja1.delete(0,END)))

botonE = Button(bd=0, text='/', font=('ubuntu',24),
command=lambda:(lista2.insert(0,Operacion(caja1.get(),"di")),
lista1.insert(0,caja1.get()),caja1.delete(0,END)))

botonRa = Button(bd=0, text='R2', font=('ubuntu',24),
command=lambda:(lista2.insert(0,Raiz(caja1.get())),
lista1.insert(0,caja1.get()),caja1.delete(0,END)))

botonIg = Button(bd=0, text='=', font=('ubuntu',24),
command=lambda:(lista2.insert(0,Igual(caja1.get())),
lista1.insert(0,"---------",caja1.get()),caja1.delete(0,END)))

#Boton del punto
botonPnt = Button(bd=0, text='.', font=('ubuntu',24),
command=lambda:caja1.insert(END,"."))

#Boton Clear
botonClr = Button(bd=0, text='CE', font=('ubuntu',20),
command=lambda:(Clear(),lista1.delete(0,END),lista2.delete(0,END),
caja1.delete(0,END)))

boton7.place(height=40, width=40,x=10,y=140)
boton8.place(height=40, width=40,x=55,y=140)
boton9.place(height=40, width=40,x=100,y=140)
boton4.place(height=40, width=40,x=10,y=185)
boton5.place(height=40, width=40,x=55,y=185)
boton6.place(height=40, width=40,x=100,y=185)
boton3.place(height=40, width=40,x=100,y=230)
boton2.place(height=40, width=40,x=55,y=230)
boton1.place(height=40, width=40,x=10,y=230)
boton0.place(height=40, width=85,x=10,y=275)
botonS.place(height=40, width=40,x=145,y=140)
botonR.place(height=40, width=40,x=145,y=185)
botonP.place(height=40, width=40,x=190,y=140)
botonE.place(height=40, width=40,x=190,y=185)
botonRa.place(height=40, width=40,x=145,y=230)
botonIg.place(height=85, width=40,x=190,y=230)
botonPnt.place(height=40, width=40,x=100,y=275)
botonClr.place(height=40, width=40,x=145,y=275)


gui.mainloop()
