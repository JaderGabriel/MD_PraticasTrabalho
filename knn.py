import pearson
import manipular_files
import os

d = manipular_files.gerar_dicionário_dados1()
linha_a_processar = [0]

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
def mais_proximos_filmes(todos, usuario):
    user_chaves= []
    todos_chaves = []
    usuario_unico = []
    teste = []
    for i in usuario:
        user_chaves.append((i[0], i[1]))
    d_usuario=dict(user_chaves)
    registros_totais = len(todos)

    usuario_unico = buscar_pelo_usuario(id_user='%s' %'1',todos=todos,linha_final=registros_totais,linha_inicial=0)

def buscar_pelo_usuario(id_user, todos,linha_final,linha_inicial):
    lista_user = []
    limite = 0
    for i in range(0,50):
        if todos[(linha_inicial)][0] == '%s' %id_user:
           lista_user.append((todos[(i)][1],todos[(i)][2] ))
           print(todos[(i)][0],todos[(i)][1])
           limite += 1

        else:
            print(limite)
            break
        #elif todos[(i)][0] != '%s' %id_user:

    return lista_user

