import criar_dicionário
d = criar_dicionário.gerar_dicionário_dados1()
def soma_manhattan(user1, user2):
    manhattan = 0
    ## usar depois para ver se os dois dict tem as mesmas chaves
    listaKey1 = user1.keys()
    listaKey2 = user2.keys()
    for i in listaKey1:
        if(user1[(i)] != '-' and user2[(i)] != '-' ):
            coord = abs(float(user1[(i)]) - float(user2[(i)]))
            manhattan += coord
    return manhattan

def sugerir_manhattan(dicionario_completo, usuario_a_sugerir, lista_das_distancias):
   lista_mais_proximo = sorted(lista_das_distancias)
   sugerir = []
   for sugestoes in dicionario_completo[lista_mais_proximo[0][1]]:
       if(d[usuario_a_sugerir][sugestoes] == '-' and d[lista_mais_proximo[0][1]][sugestoes] != '-'):
           sugerir.append(sugestoes)
   return sugerir
