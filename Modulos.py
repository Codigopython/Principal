valor = 0
operacion = ""
def Suma(num):
    global valor
    global operacion
    operacion = "suma"
    valor = valor+int(num)
    return valor

def Resta(num):
    global valor
    global operacion
    operacion = "resta"
    if valor == 0:
        valor = int(num)
        return valor
    else:
        valor = valor-int(num)
        return valor

def Multi(num):
    global valor
    global operacion
    operacion = "multi"
    if valor == 0:
        valor = 1
        valor = valor*int(num)
        return valor
    else:
        valor = valor*int(num)
        return valor

def Divi(num):
    global valor
    global operacion
    operacion = "divi"
    if valor == 0:
        valor = int(num)
        return valor
    else:
        valor = valor/int(num)
        return valor

def Igual(num):
    global valor
    global operacion

    if operacion == "suma":
        valor = valor+int(num)
        return valor

    elif operacion == "resta":
        valor = valor-int(num)
        return valor

    elif operacion == "multi":
        valor = valor*int(num)
        return valor

    elif operacion == "divi":
        valor = valor/int(num)
        return valor

    else:
        print ("algo anda mal")

def Clear():
    global valor
    global operacion
    operacion = ""
    valor = 0
