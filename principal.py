#encoding = utf-8
#!/usr/bin/ python
from datetime import datetime
import knn
import manhattan
import manipular_files
import listar_diretorio as dir
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

d = manipular_files.gerar_dicionário_dados1()
# Resposta questao 1a
distancia = manhattan.soma_manhattan(user1=d['Ana'],user2=d['Jessica'])
print("DISTANCIA DE MANHATTAN ENTRE %s e %s: %.3f\n" %('Ana','Jessica', distancia))
print("QUESTAO 1e\n")
m = knn.mais_proximos(use1='Jessica',dicionario_completo=d,k=3)
recomendacao = knn.sugerir_por_knn(a_sugerir='Jessica',lista_ordenada=m,artista='B.B. King')
print("\nQUESTAO 4a:\n")
items_filmes = dir.listar_diretorio()
items_cerveja = dir.listar_diretorio2()
bd_cerveja = manipular_files.obter_dados_cerveja(items_cerveja[0])
manipular_files.gerar_dicionario_cervejas(lista_dados=bd_cerveja)

limite_superior = len(items_filmes)
for i in range (3,limite_superior):
    print('\n---------------------------------------')
    print(items_filmes[(i)])
    var_input = manipular_files.gerar_dicionario_filmes(s='%s' %(items_filmes[(i)]))
    print('NUMERO DE ELEMENTOS DA LISTA %s: '%items_filmes[(i)],len(var_input))
#criar_dicionário.gerar_dicionario_filmes(s='ub.test')



