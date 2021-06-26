import random

x0 = []
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []



def eleccion_de_cantidad():
    print ("Cual sera el numero de repeticiones?")
    
    repnum = input()

    try:
        repnum = int(repnum)
    except:
        print("No se ingreso un numero valido")
    
    for i in range(0, repnum):
        x = random.randrange(0,6)
        if x == 0:
            x0.append(x)
        elif x == 1:
            x1.append(x)
        elif x == 2:
            x2.append(x)
        elif x == 3:
            x3.append(x)
        elif x == 4:
            x4.append(x)
        elif x == 5:
            x5.append(x)

   

def calculos_y_datos():
    x0len = len(x0)
    x1len = len(x1)
    x2len = len(x2)
    x3len = len(x3)
    x4len = len(x4)
    x5len = len(x5)

    print("Cantidad de numero 0=", x0len)
    print("Cantidad de numero 1=", x1len)
    print("Cantidad de numero 2=", x2len)
    print("Cantidad de numero 3=", x3len)
    print("Cantidad de numero 4=", x4len)
    print("Cantidad de numero 5=", x5len)

    xlentotal = x0len + x1len + x2len + x3len + x4len + x5len

    xmaxnum = xlentotal * 5
    print("El maximo numero hubiese sido", xmaxnum)

    print("El numero minimo hubiese sido 0")

    x0porc = (x0len * 100) / xlentotal
    x1porc = (x1len * 100) / xlentotal
    x2porc = (x2len * 100) / xlentotal
    x3porc = (x3len * 100) / xlentotal
    x4porc = (x4len * 100) / xlentotal
    x5porc = (x5len * 100) / xlentotal

    print("Un", x0porc, "porciento de los numeros es 0")
    print("Un", x1porc, "porciento de los numeros es 1")
    print("Un", x2porc, "porciento de los numeros es 2")
    print("Un", x3porc, "porciento de los numeros es 3")
    print("Un", x4porc, "porciento de los numeros es 4")
    print("Un", x5porc, "porciento de los numeros es 5")




        
if __name__ == '__main__':
    print("Hola! El objetivo de este programa es calcular si es en verdad aleatoria la funcion de python!")
    
    eleccion_de_cantidad()
    
    calculos_y_datos()

    print ("Listo! Finalizamos, espero que te guste!")
