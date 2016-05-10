valor = 0
est = ""

def Suma(num):
    global valor
    valor = valor+int(num)
    return valor

def Resta(num):
    global valor
    if valor == 0:
        valor = int(num)
        return valor
    else:
        valor = valor-int(num)
        return valor

def Multi(num):
    global valor
    if valor == 0:
        valor = 1
        valor = valor*int(num)
        return valor
    else:
        valor = valor*int(num)
        return valor

def Divi(num):
    global valor
    if valor == 0:
        valor = int(num)
        return valor
    else:
        valor = valor/int(num)
        return valor

def Operacion(num,op):
    global est
    if est == "":
        est = op
    if num =="":
        est = op
    if est == "s":
        suma = Suma(num)
        est = op
        return suma
    if est == "r":
        resta = Resta(num)
        est=op
        return resta
    if est == "m":
        multi = Multi(num)
        est=op
        return multi
    if est == "d":
        divi = Divi(num)
        est=op
        return divi
    else:
        print("algo esta mal")

def Igual(num):
    global est
    global op
    if op == "s":
        Suma(num)
        est=""
        return valor
    elif op == "r":
        Resta(num)
        est=""
        return valor
    elif op == "m":
        Multi(num)
        est=""
        return valor
    elif op == "d":
        Divi(num)
        est=""
        return valor
    else:
        print ("algo anda mal")

def Clear():
    global valor
    global est
    est = ""
    valor = 0
