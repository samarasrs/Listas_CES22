import math



def sum_of_squares(lista):
    soma=0
    for i in lista:
        soma=soma+math.pow(i,2)
    return soma

'''
print(sum_of_squares([2,3,4])==29)
print(sum_of_squares([])==0)
print(sum_of_squares([2,-3,4])==29)
'''