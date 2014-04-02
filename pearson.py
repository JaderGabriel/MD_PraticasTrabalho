import math
import matplotlib.pyplot as plt
import numpy as np

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


    dividendo = (somatorio1 - (somatorioX*somatorioY/n))
    divisor = math.sqrt(x2-(somatorioX**2/n)) * math.sqrt(y2-(somatorioY**2/n))
    if(divisor != 0):
        coeficiente = dividendo/divisor
    #print( dividendo, divisor)
    return coeficiente
def gerar_grafico(user1, user2, d):
    # ArrayX  = [ 200, 201, 202, 203 ]
    # ArrayY  = [ 120, 232, 200, 54 ]
    #
    # plt.title("Grafico de Pearson para %s e %s" %(user1,user2), fontsize = 20)
    # plt.bar(ArrayX, ArrayY, 10 )
    # plt.xlabel("Year", fontsize = 15)
    #
    # plt.ylabel("Number of teachers", fontsize = 15)
    # plt.xlim(200, 203)
    # plt.show()
    print(user1)
    print(d[user1])

    listaX_user1 = []
    listaY_user2 = []
    lista_chaves = d[user1].keys()
    plt.title("Grafico de Pearson para %s e %s" %(user1,user2), fontsize = 20)
    plt.bar(listaX_user1, listaY_user2, 10 )
    plt.show()
