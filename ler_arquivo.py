#encoding = utf-8
#!/usr/bin/ python
import csv
import pprint
from datetime import datetime
import math
import manhattan
import criar_dicionário
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
def conficiente_pearson(user1, user2):

    r = range (0,10)
    print(r)
    return r


for user1 in d:
    manhattan_proximidade = []
    for user2 in d:
        if(user1 != user2):
            manhattan.soma_manhattan(user1=d[user1], user2=d[user2])
            manhattan_proximidade.append((manhattan,user2))
            #print("\nSoma de Manhattan entre %s e %s = %.2f" %(user1,user2,manhattan))
    sugestao_a_usuario = manhattan.sugerir_manhattan(dicionario_completo=d,usuario_a_sugerir=user1,lista_das_distancias=manhattan_proximidade)
    print("\nSegundo a formula de proximidade de Manhattan: \n%s gostará de %s" %(user1,sugestao_a_usuario))
    manhattan_proximidade= []

"""
Usuario = input("\n\nNome do Usuário\n")
Artista= input("Nome do Artista\n\n")
user = str(Usuario)
artst = str(Artista)
teste = d.get(user)
teste2 = teste.get(artst)
if not teste or not teste2:
    print('DONT MATCH')
elif teste and teste2:
    print("Nota aferida por %s a %s, caso essa combinaçao exista:\n" %(user,artst))
    print(d[user][artst])
    """
f.write("end of file")
f.close()


