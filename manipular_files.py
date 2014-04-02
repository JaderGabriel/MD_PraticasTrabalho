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
      artista_nota = []

      nota = []

      nota_por_artista = []

    return d
def gerar_dicionario_filmes(s):
    """
    Gera dicionário do arquivo que se receber no parametro s, desde que esse esteja na pasta '/ml-100k'
    """
    dados = csv.reader(open("ml-100k/%s" %(s),"r"))
    print (dados)
    dados2 = []
    a_procurar = 1
    for i in dados:
        dados2.append(i)
    return dados2
def obter_dados_cerveja(s):
    dados = csv.reader(open("beer_reviews/%s" %(s),"r"))
    print (dados)
    dados2 = []
    a_procurar = 1
    for i in dados:
        dados2.append(i)
    return dados2
def gerar_dicionario_cervejas(lista_dados):
    atributos_cerveja = []
    atrb = []
    for i in lista_dados[0]:
        atributos_cerveja.append((i,()))
        atrb.append(i)
    dic_atributos = dict(atributos_cerveja)
    print(atrb)
    limite_superior = len(lista_dados)
    for i in range (1,limite_superior):
        if 'Brahma' in lista_dados[(i)]:
            print(lista_dados[(i)])
