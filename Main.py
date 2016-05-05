from tkinter import *
from Modulos import *
#frame principal
gui = Tk()
gui.title('Calculadora')
gui.geometry('200x300+2000+1')
gui.config(bg='white')

#Caja de operaciones
lista1 = Listbox(bd=0,height=3)
lista1.pack()

caja1 = Entry(bd=0)
caja1.pack()

#botones del 0 al 9
boton1 = Button(bd=0, text='7', font=('ubuntu',24),
command=lambda: caja1.insert(END,'7'))
boton1.place(height=40, width=40,x=10,y=70)

boton1 = Button(bd=0, text='8', font=('ubuntu',24),
command=lambda: caja1.insert(END,'8'))
boton1.place(height=40, width=40,x=55,y=70)

boton1 = Button(bd=0, text='9', font=('ubuntu',24),
command=lambda: caja1.insert(END,'9'))
boton1.place(height=40, width=40,x=100,y=70)

boton1 = Button(bd=0, text='4', font=('ubuntu',24),
command=lambda: caja1.insert(END,'4'))
boton1.place(height=40, width=40,x=10,y=115)

boton1 = Button(bd=0, text='5', font=('ubuntu',24),
command=lambda: caja1.insert(END,'5'))
boton1.place(height=40, width=40,x=55,y=115)

boton1 = Button(bd=0, text='6', font=('ubuntu',24),
command=lambda: caja1.insert(END,'6'))
boton1.place(height=40, width=40,x=100,y=115)

boton1 = Button(bd=0, text='3', font=('ubuntu',24),
command=lambda: caja1.insert(END,'3'))
boton1.place(height=40, width=40,x=100,y=160)

boton1 = Button(bd=0, text='2', font=('ubuntu',24),
command=lambda: caja1.insert(END,'2'))
boton1.place(height=40, width=40,x=55,y=160)

boton1 = Button(bd=0, text='1', font=('ubuntu',24),
command=lambda: caja1.insert(END,'1'))
boton1.place(height=40, width=40,x=10,y=160)

boton1 = Button(bd=0, text='0', font=('ubuntu',24),
command=lambda: caja1.insert(END,'0'))
boton1.place(height=40, width=40,x=10,y=205)

#Botones de operaciones matematicas
boton1 = Button(bd=0, text='-', font=('ubuntu',24),
command=lambda: (Operacion("resta"), lista1.insert(END,
Captura1(int(caja1.get()))),caja1.delete(0,END)))
boton1.place(height=85, width=40,x=145,y=70)

boton1 = Button(bd=0, text='+', font=('ubuntu',24),
command=lambda: (Operacion("suma"), lista1.insert(END,
Captura1(int(caja1.get()))), caja1.delete(0,END)))
boton1.place(height=85, width=40,x=145,y=160)

#Boton igual
boton1 = Button(bd=0, text='=', font=('ubuntu',24),
command=lambda: (lista1.insert(END, Captura2(int(caja1.get())),
caja1.delete(0,END)), lista1.insert(END, Calculo())))
boton1.place(height=40, width=40,x=55,y=205)

#Boton Clear
boton1 = Button(bd=0, text='CE', font=('ubuntu',20),
command=lambda: (caja1.delete(0,END), lista1.delete(0,END)))
boton1.place(height=40, width=40,x=100,y=205)

gui.mainloop()
