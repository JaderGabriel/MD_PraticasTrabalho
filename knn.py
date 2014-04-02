import pearson
import manipular_files
d = manipular_files.gerar_dicionário_dados1()

def mais_proximos(use1, dicionario_completo, k):
    pearson_proximidade = []
    g = []
    for user2 in dicionario_completo:

        if (user2 != use1):
            coeficiente = pearson.calcular_coeficiente(user1=dicionario_completo[use1],user2=dicionario_completo[user2])
            #print(coeficiente, user2)
            if coeficiente:
                pearson_proximidade.append((coeficiente,user2))

    m=sorted(pearson_proximidade)
    x=m.reverse()
    for i in range(0,k):
        g.append(m[i])
    print("Lista de k mais proximos à %s:\n" %(use1),g)

    return g

def sugerir_por_knn(a_sugerir,lista_ordenada, artista):
    total = 0
    lista_influencia = []
    recomendaçao = 0
    for i in lista_ordenada:
        total += i[0]
    for i in lista_ordenada:
        recomendaçao += i[0]/total * float(d[(i[1])][artista])
        #float(i[0]/total,i[1]) * float(d[(i[1])][artista])

    print("Recomandaçao por KNN à %s de %s :\n" %(a_sugerir,artista),recomendaçao)
