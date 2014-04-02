import os
_data__ = '01/04/14'
def listar_diretorio():
    items = os.listdir('ml-100k')
    #print(os.listdir('ml-100k'))
    return items
def listar_diretorio2():
    items = os.listdir('beer_reviews')
    return items

    
