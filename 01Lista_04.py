def sum_list_to_even(lista):
    soma=0
    for i in lista:
        if i%2!=0:
            soma=soma+i
        else:
            return soma
    return soma


'''
A cada elemento da lista verifica-se se é par se não for seu
valor é incrementado à variavel soma se for par o loop for é interrompido
caso não haja nenhum número par na lista a função retorna a soma de todos os valores
da lista
'''

