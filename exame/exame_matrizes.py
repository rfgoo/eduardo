from random import seed
from random import choices
from random import randint
seed(9730)
r=[
[4, 4, 9, 1],
[2, 6, 8, 2],
[2, 5, 1, 3] ]

def c(matrix, num):
    res = []

    for linha, i in enumerate(matrix):
        for col, j in enumerate(i):
            if j == num:
                res.append([linha, col])
    return res

def f(matrix):
    sum = 0
    for i in matrix: # linhas
        for j in i:
           sum += j
    return sum

p_1 = c(r, 3)
p_2 = f(p_1)
print(p_1)
print(p_2)
p_3 = c(r, 2)
p_4 = f(p_3)
print(p_3)
print(p_4)

def get_random_matrix():
    n_lines   = randint(100, 200)
    n_columns = randint(100, 200)
    lines = []
    for x in range(n_lines):
        lines.append(choices(range(-100, 100), k=n_columns))
    return lines

r_1 = get_random_matrix()
r_2 = get_random_matrix()
r_3 = get_random_matrix()
r_4 = get_random_matrix()
r_5 = get_random_matrix()

print('só para verificação dos valores pseudoaleatórios gerados')
print(r_5[0][0])
print(r_5[0][1])
print(r_5[1][0])
print(r_5[1][1])

# 2.1 A soma de todos os índices de linha e de coluna, da matriz r_1, onde está o número -56, é 24939.
print(f(c(r_1,-56)))
print(f(c(r_1,-56)) == 24939)

