def Operacion(a):
    global operacion
    operacion = a
    print(operacion)

def Captura1(num1):
    global dato1
    dato1 = num1
    print("captura1>> ", dato1)
    return dato1

def Captura2(num2):
    global dato2
    dato2 = num2
    print("captura2>> ", dato2)
    return dato2

def Calculo():
    if operacion == "suma":
        suma = dato1 + dato2
        print("operacion>> ",suma)
        return "Suma",suma
    elif operacion == "resta":
        resta = dato1 - dato2
        print("operacion>> ", resta)
        return "Resta",resta
    else:
        print("algo esta mal")
