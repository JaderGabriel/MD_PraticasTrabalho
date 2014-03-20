__author__ = "Jader Gabriel\n"
_data__ = '20/03/14'
import pprint
import csv
def gerar_dicionário():
    dados = csv.reader(open("dados1.csv","r"))
    linha_gerais = []
    linha_Artistas = []
    prof_notas = []
    dicionario = []
    artista_nota = []
    nota = []
    nota_por_artista = []
    f = open("dados_ordenados.txt","w")
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


    return d
