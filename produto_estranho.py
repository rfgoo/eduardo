from random import seed
from random import choices
from random import randint
seed(3417)
w_a = [
    [4, 3, 2],
[2, 4, 3] ]

w_b = [
[1,-1, 1],
[-1, 1, -1] ]

def s(mat1, mat2):
    sum =0
    for i in range(len(mat1)): # i por linha
        for j in range(len(mat1[0])): # j por numero na linha
            sum += mat1[i][j]*mat2[i][j]
    return sum

f = s(w_a, w_b)
print(f)


def get_random_matrices():
    n_lines   = randint(100, 200)
    n_columns = randint(100, 200)
    lines_1 = []
    lines_2 = []
    for x in range(n_lines):
        lines_1.append(choices(range(-100, 100), k=n_columns))
        lines_2.append(choices(range(-100, 100), k=n_columns))
    return (lines_1, lines_2)

(w_1, w_2) = get_random_matrices()
(w_3, w_4) = get_random_matrices()
(w_5, w_6) = get_random_matrices()
(w_7, w_8) = get_random_matrices()
(w_9, w_10) = get_random_matrices()


print('só para verificação dos valores pseudoaleatórios gerados')
print(w_10[0][0])
print(w_10[0][1])
print(w_10[1][0])
print(w_10[1][1])