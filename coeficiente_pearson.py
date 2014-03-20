import math
def calcular_coeficiente(user1, user2):
    somatorio1 = 0
    somatorioX=0
    somatorioY =0
    x2 = 0
    y2 = 0
    coeficiente = 0
    n = 0
    listaKey1 = user1.keys()
    for i in listaKey1:
        if(user1[(i)] !="-" and user2[(i)] !="-"):
            n += 1
            x = float(user1[(i)])
            y = float(user2[(i)])
            somatorio1 += x*y
            somatorioX += x
            somatorioY += y
            x2 += x**2
            y2 += y**2

    #print("somamamamaa")
    #print(user1, user2)
    dividendo = (somatorio1 - (somatorioX*somatorioY/n))
    divisor = math.sqrt(x2-(somatorioX**2/n)) * math.sqrt(y2-(somatorioY**2/n))
    if(divisor != 0):
        coeficiente = dividendo/divisor
    #print( dividendo, divisor)
    return coeficiente



