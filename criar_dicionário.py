__author__ = "Jader Gabriel\n"
_data__ = '20/03/14'
import pprint
import csv
import ldap3 as ld

def gerar_dicionário_dados1():

    # noinspection PyPep8
    dados = csv.reader(open("dados1.csv","r"))
    linha_gerais = []
    linha_Artistas = []
    prof_notas = []
    dicionario = []
    artista_nota = []
    nota = []
    nota_por_artista = []

    for linhas in dados:
      # noinspection PyPep8
      linha_gerais.append(linhas)
    # noinspection PyPep8,PyPep8
    for x in range (1,9):
      # noinspection PyPep8
      linha_Artistas.append(linha_gerais[(x)][0])
      # noinspection PyPep8
      prof_notas.append(linha_gerais[0][(x)])
    # noinspection PyPep8,PyPep8
    for x in range (0,8):
      # noinspection PyPep8
      nome = prof_notas[(x)]
      # noinspection PyPep8,PyPep8
      dicionario.append((nome,()))
      # noinspection PyPep8
      d = dict(dicionario)
    # noinspection PyPep8,PyPep8
    for x in range (0,8):
      # noinspection PyPep8
      nome2 = prof_notas[(x)]

      # noinspection PyPep8,PyPep8,PyPep8
      for m in range (0,8):
        artista_nota.append(linha_Artistas[m])
        nota.append(linha_gerais[m+1][x+1])
        # noinspection PyPep8
        nota_por_artista.append((linha_Artistas[m] , linha_gerais[m+1][x+1]))
      # noinspection PyPep8
      dicionario_notas_dadas = dict(nota_por_artista)
      # noinspection PyPep8
      d[nome2] = dicionario_notas_dadas
      #print("\n")
      #pprint.pprint("NOTAS DADAS POR  %s A:--"  % prof_notas[(x)])

      #print(d[prof_notas[(x)]])
      #print ("%-20s-+-%-7s" %("-" * 20, "-" * 7))
      #print ("%-20s : %-7s" %("Nome", "Nota"))
      #print ("%-20s-+-%-7s" %("-" * 20, "-" * 7))
      #for i in range(0,8):
          #print("%-20s | %1s" %(artista_nota[(i)], nota[(i)]))
      #print ("%-20s-+-%-7s" %("-" * 20, "-" * 7))


      # noinspection PyPep8,PyPep8
      artista_nota = []
      # noinspection PyPep8
      nota = []
      # noinspection PyPep8
      nota_por_artista = []


    # noinspection PyPep8
    return d
def gerar_dicionario_filmes():
    dados = csv.reader(open("ml-100k/u.data","r"))
    print (dados)
    dados2 = []
    for i in dados:
      dados2.append(i)
    dados2 = sorted(dados2)
    for m in dados2:
        print(m)
