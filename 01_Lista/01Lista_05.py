
def count_words (lista):
    cont=0
    if "sam" in lista:
        cont=lista.index("sam")+1
    else:
        cont=lista.__len__()
    return cont

'''
lista = ['aba', 'ksdhflka','hflkasdf', 'ududu', 'kkk', '1', 'sam','lalala','rsrsr']
print(count_words(lista))
7
'''

'''
Primeiro verifica-se se exite a palavra "sam" na lista
caso exista lista.index("sam") retorna o indice da primeira
ocorrencia da palavra "sam" e portanto a contagem é o indice+1 visto que
os indices das listas começam em 0.
Caso nao exista a palavra "sam" a contagem é o tamanho da lista.
''' 