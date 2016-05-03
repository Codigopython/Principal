from tkinter import *

#frame principal
gui = Tk()
gui.title('Calculadora')
gui.geometry('200x300+2000+1')
gui.config(bg='white')

#Caja de operaciones

lista1 = Listbox(bd=1,height=2)
lista1.pack()

caja1 = Entry(bd=2)
caja1.pack()

#botones del 0 al 9
boton1 = Button(text='7', font=('ubuntu',24))
boton1.place(height=40, width=40,x=10,y=70)

boton1 = Button(text='8', font=('ubuntu',24))
boton1.place(height=40, width=40,x=55,y=70)

boton1 = Button(text='9', font=('ubuntu',24))
boton1.place(height=40, width=40,x=100,y=70)

boton1 = Button(text='4', font=('ubuntu',24))
boton1.place(height=40, width=40,x=10,y=115)

boton1 = Button(text='5', font=('ubuntu',24))
boton1.place(height=40, width=40,x=55,y=115)

boton1 = Button(text='6', font=('ubuntu',24))
boton1.place(height=40, width=40,x=100,y=115)

boton1 = Button(text='3', font=('ubuntu',24))
boton1.place(height=40, width=40,x=100,y=160)

boton1 = Button(text='2', font=('ubuntu',24))
boton1.place(height=40, width=40,x=55,y=160)

boton1 = Button(text='1', font=('ubuntu',24),
command=lambda: caja1.insert(END,'1'))
boton1.place(height=40, width=40,x=10,y=160)

boton1 = Button(text='0', font=('ubuntu',24),
command=lambda: caja1.insert(END,'0'))
boton1.place(height=40, width=40,x=10,y=205)

#Boton Clear
boton1 = Button(text='=', font=('ubuntu',24))
boton1.place(height=40, width=85,x=55,y=205)

#Botones de operaciones matematicas
boton1 = Button(text='-', font=('ubuntu',24),
command=lambda: caja1.insert(END,'-'))
boton1.place(height=85, width=40,x=145,y=70)

boton1 = Button(text='+', font=('ubuntu',24),
command=lambda: caja1.insert(END,'+'))
boton1.place(height=85, width=40,x=145,y=160)



# button1.place(bordermode=OUTSIDE, height=40, width=40, y=70)


gui.mainloop()
