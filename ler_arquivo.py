#encoding = utf-8
#!/usr/bin/ python
import csv
import pprint
from datetime import datetime
import math

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

dados = csv.reader(open("dados1.csv","r"))

linha_gerais = []
linha_Artistas = []
prof_notas = []
dicionario = []
artista_nota = []
nota = []
nota_por_artista = []
f = open("dados_ordenados.txt","w")

inicio(f)

for linhas in dados:
  linha_gerais.append(linhas)
for x in range (1,9):
  linha_Artistas.append(linha_gerais[(x)][0])
  prof_notas.append(linha_gerais[0][(x)])
for x in range (0,8):
  nome = prof_notas[(x)]
  dicionario.append((nome,()))
  d = dict(dicionario)
for x in range (0,8):
  nome2 = prof_notas[(x)]

  for m in range (0,8):
    artista_nota.append(linha_Artistas[m])
    nota.append(linha_gerais[m+1][x+1])
    nota_por_artista.append((linha_Artistas[m] , linha_gerais[m+1][x+1]))
  dicionario_notas_dadas = dict(nota_por_artista)
  d[nome2] = dicionario_notas_dadas
  print("\n")
  pprint.pprint("NOTAS DADAS POR  %s A:--"  % prof_notas[(x)])
  f.write("\n\nNOTAS DADAS POR  %s A:--\n"  % prof_notas[(x)])
  print(d[prof_notas[(x)]])
  #print ("%-20s-+-%-7s" %("-" * 20, "-" * 7))
  #print ("%-20s : %-7s" %("Nome", "Nota"))
  #print ("%-20s-+-%-7s" %("-" * 20, "-" * 7))
  f.write("%-20s-+-%-7s\n" %("-" * 20, "-" * 7))
  f.write("%-20s : %-7s\n" %("Nome", "Nota"))
  f.write("%-20s-+-%-7s\n" %("-" * 20, "-" * 7))
  for i in range(0,8):
      #print("%-20s | %1s" %(artista_nota[(i)], nota[(i)]))
      f.write("%-20s | %1s\n" %(artista_nota[(i)], nota[(i)]))
  #print ("%-20s-+-%-7s" %("-" * 20, "-" * 7))
  f.write("%-20s-+-%-7s\n" %("-" * 20, "-" * 7))

  artista_nota = []
  nota = []
  nota_por_artista = []
for user1 in d:
    for user2 in d:
        if(user1 != user2):
            manhattan = soma_manhattan(d[user1], d[user2])
            print(" Soma de Manhattan entre %s e %s = %.2f" %(user1,user2,manhattan))
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


