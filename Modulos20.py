#version 2.1
#by kelvin romani ollero
x = 0
est = False
opMain = "0x"
print (est, x, opMain)
#################################
def Suma(y):
    global x
    x = x + float(y)
    return x

def Resta(y):
    global x
    x = x - float(y)
    return x

def Multi(y):
    global x
    x = x * float(y)
    return x

def Divi(y):
    global x
    x = x / float(y)
    return x

def Clear():
    global x
    global est
    global opMain
    x = 0
    est = False
    opMain = "0x"
########################################
def Operacion(y,op):
    global est
    global x
    global opMain

    if est == False:
        if y == "":
            return "Introduce un valor"

    if est == False:
        if opMain == "0x":
            x = float(y)
            opMain = op
            est = True
            return x

    if est == True:
            if y != "":
                x = Selector(y)
                opMain = op
                return x

    if est == True:
            if y == "":
                opMain = op

######################################
def Selector(y):
    global opMain
    if opMain == "su":
        return Suma(y)

    if opMain == "re":
        return Resta(y)

    if opMain == "mu":
        return Multi(y)

    if opMain == "di":
        return Divi(y)

    else:
        print("algo anda mal (f:Operacion)")

def Igual(y):
    return Selector(y)

def Raiz(y):
    global x
    if est == True:
        y = x
        x = int(y)**(1/2)
        return x

    if est == False:
        x = int(y)**(1/2)
        return x
