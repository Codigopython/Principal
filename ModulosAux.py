valor=0
def Suma(num):
    global valor
    valor = valor+int(num)
    print (valor)
    return "+", valor

def Resta(num):
    global valor
    valor = valor-int(num)
    print (valor)
    return "-", valor

def Clear():
    global valor
    valor = 0
