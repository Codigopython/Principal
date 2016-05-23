estV = False
valor = 0
est = ""

def Suma(num):
    global valor
    valor = valor+float(num)
    return valor

def Resta(num):
    global valor
    if estV == False:
        valor = float(num)
        return valor
    else:
        valor = valor-float(num)
        return valor

def Multi(num):
    global valor
    global estV
    if estV == False:
        valor = 1
        print("multi")
        valor = valor*float(num)
        estV = True
        return valor
    else:
        valor = valor*float(num)
        return valor

def Divi(num):
    global valor
    if valor == 0:
        valor = float(num)
        return valor
    else:
        valor = valor/float(num)
        return valor

def Raiz(num):
    global valor
    if valor == 0:
        valor = float(num)**(1/2)
        return valor
    else:
        valor = valor**(1/2)
        return valor

def Operacion(num,op):
    global est
    if est == "":
        est = op
    if num =="":
        a="Introdusca un valor"
        est = op
        return a
    if est == "s":
        su = Suma(num)
        print(su)
        est = op
        return su
    if est == "r":
        re = Resta(num)
        est=op
        return re
    if est == "m":
        mu = Multi(num)
        est=op
        return mu
    if est == "d":
        di = Divi(num)
        est=op
        return di
    if est == "ra":
        ra = Raiz(num)
        return ra
    else:
        print("algo esta mal(fOperacion)")

def Igual(num):
    global est
    global valor
    if num =="":
        a="Introdusca un valor"
        return a
    if est == "s":
        suma = Suma(num)
        est=""
        valor=0
        return suma
    elif est == "r":
        resta = Resta(num)
        est=""
        valor=0
        return resta
    elif est == "m":
        multi = Multi(num)
        est=""
        valor=0
        return multi
    elif est == "d":
        divi = Divi(num)
        est=""
        valor=0
        return divi
    else:
        print ("algo anda mal(fIgual)")

def Clear():
    global valor
    global est
    est = ""
    valor = 0
