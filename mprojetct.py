import manhattan
import criar_dicionário
import pearson
d = criar_dicionário.gerar_dicionário()
for user1 in d:
    manhattan_proximidade = []
    for user2 in d:
        if(user1 != user2):
            print("\nRelaçoes entre %s e %s" %(user1,user2))
            manhattan.soma_manhattan(user1=d[user1], user2=d[user2])
            manhattan_proximidade.append((manhattan,user2))
            coeficiente_p = pearson.calcular_coeficiente(user1=d[user1],user2=d[user2])

            print("COEFICIENTE DE PEARSON: %s " %coeficiente_p)
            #pearson.gerar_grafico(user1=user1,user2=user2,d=d)
    sugestao_a_usuario = manhattan.sugerir_manhattan(dicionario_completo=d,usuario_a_sugerir=user1,lista_das_distancias=manhattan_proximidade)
    print("Segundo a formula de proximidade de Manhattan: \n%s gostará de %s" %(user1,sugestao_a_usuario))
    manhattan_proximidade= []
