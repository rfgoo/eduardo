from random import seed
from random import choices
from random import randint
seed(9088)
x=[
[4, 3, 9],
[2, 6, 8],
[7, 5, 1] ]

def c(matrix):

    # criar uma matrix do mm tamanho so com zeros
    result = [[0 for i in range(len(matrix))] for j in range(len(matrix))]

    # fazer a trasposição da matriz (trocar linhas por colunas)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j]=matrix[j][i]
    sum = 0
    # soma das colunas da matrix original é a soma das linhas da matriz transposta
    # se puderes usar o sum(lista) era mais facil
    soma_colunas=[]
    for linha in result:
        # sum = sum(linha)
        for numero in linha:
           sum += numero
        soma_colunas.append(sum)
        sum = 0
    return soma_colunas


def c2(matrix):
    # sem transpor
    sum = 0
    soma_colunas = []
    for i in range(len(matrix)): # tenho as linhas
        for j in range(len(matrix[0])): # tenho as colunas
           sum += matrix[j][i]
           print(matrix[j][i])
        soma_colunas.append(sum)
        sum = 0

    return soma_colunas

n = c2(x)
print(n)
def get_random_matrix():
    n_lines   = randint(100, 200)
    n_columns = randint(100, 200)
    lines = []
    for x in range(n_lines):
        lines.append(choices(range(-100, 100), k=n_columns))
    return lines


x_1 = get_random_matrix()
x_2 = get_random_matrix()
x_3 = get_random_matrix()
x_4 = get_random_matrix()
x_5 = get_random_matrix()


print('só para verificação dos valores pseudoaleatórios gerados')
print(x_5[0][0])
print(x_5[0][1])
print(x_5[1][0])
print(x_5[1][1])