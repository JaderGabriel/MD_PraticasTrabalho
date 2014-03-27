#encoding = utf-8
#!/usr/bin/ python
from datetime import datetime

import manhattan
import criar_dicionário
import pearson


def inicio(m):
    __author__ = "Jader Gabriel\n"
    __copyright__ = "\nCopyright 2013\n"
    __tags__ = ["Unimontes", "CCET", "DCC",
                    "Mineraçao de Dados", "Prfº: Rene Veloso"]
    __ta__ = __tags__.__str__()
    __license__ = "GPL"
    __version__ = "1.0.1"
    __email__ = "programacaoeti@outlook.com\n"
    __status__ = "\nTrabalho 1\n"
    _data__ = datetime.now()
    m.write(__author__)
    m.write(__email__)
    m.write("Ultima atualizacao: ")
    m.write(datetime.now().__str__())
    m.write(__copyright__)
    m.write(__ta__)
    m.write(__status__)
d = criar_dicionário.gerar_dicionário()
f = open("dados_ordenados.txt","w")

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
f.write("end of file")
f.close()


