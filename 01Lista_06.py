import math

def is_prime(n):
    if n ==2:
        return True
    div=math.ceil(math.sqrt(n))
    for i in range(2,div+1):
        if n%i==0:
            return False
    return True


    

'''
print(is_prime(11)) 
True

print(not is_prime(35))
True

print(is_prime(19911121))
True

A data do meu nascimento não é um número primo
print(is_prime(19920508))
False

Para estimar quantos estudantes possuem a data de nascimento que representa um numero primo
é necessario realizar uma série de suposições.
considerando que todos os 100 alunos nasceram no mesmo ano.

desconsiderando o dia 29/02 pois ninguem é registrado nesse dia
eliminando o número de dias que terminam em um número par 
eliminando o número de dias que terminam em 5 (3*12=36) 
utilizando a função dias_primos e analisando 12 anos de 1990 a 2002 e fazendo uma media dos dias primos desses anos 
obteve-se 22 dias
Portanto a probabilidade de cada aluno nascer num dia primo é aproximadamente 22/365 (6%)
Logo aproximadamente 6 a cada 100 alunos nasceram em dias primos
'''

def dias_primos(year):     
    ano=str(year)

    mes=[]
    for i in range(1,13):
        if i<10:
            mes.append(str(0)+str(i))
        else:
            mes.append(str(i))

    dia=[]
    for i in range(1,32,2):
        if i<10:
            dia.append(str(0)+str(i))
        else:
            dia.append(str(i))

    dia.remove('05')
    dia.remove('15')
    dia.remove('25')

    data=[]
    for i in mes:
        for k in dia:
            if i=='02' and int(k)<28:
                data.append(int(ano+i+k))
            elif (i=='04' or i=='06' or i=='09' or i=='11') and int(k)<30:
                data.append(int(ano+i+k))
            elif i=='01' or i=='03' or i=='05' or i=='07' or i=='08' or i=='10' or i=='12':
                data.append(int(ano+i+k))

    cont=0
    for i in data:
        if is_prime(i):
            cont=cont+1 
    return cont   

soma=0
for i in range(12):
    soma=soma+dias_primos(1990+i)
media=soma/12





 