class W:

    def __init__(self, lines, col):
        self.matrix = []
        for _ in range(lines):
            self.matrix.append([0]*col)

    def __str__(self):
        a = ""

        for i in self.matrix:
            for j in i:
                a += str(j)
                a += ' '
            a += '\n'

        return a

    def __mul__(self, other):
        result = W(len(self.matrix), len(other.matrix[0]))

        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(self.matrix[0])):
                    result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return result

    def t(self, line, col, num):
        self.matrix[line - 1][col - 1] = num

    def n(self, line, col):
        return self.matrix[line - 1][col - 1]

n_lines   = 2
n_columns = 3
w_1 = W(n_lines, n_columns)
print(w_1)
for a in range(1, n_lines+1):
    for r in range(1, n_columns+1):
        w_1.t(a, r, (a-1)*n_lines+(r-1))
print('---')
print(w_1)
print(w_1.n(1, 1))
print(w_1.n(1, 2))
print(w_1.n(1, 3))
print(w_1.n(2, 1))
print(w_1.n(2, 2))
print(w_1.n(2, 3))
n_lines   = 3
n_columns = 4
w_2 = W(n_lines, n_columns)
for a in range(1, n_lines+1):
    for r in range(1, n_columns+1):
        w_2.t(a, r, 6+(a-1)*n_lines+(r-1))
print('---')
print(w_2)
w_3 = w_1 * w_2
print('---')
print(w_3)
from random import seed
from random import randint
seed(9383)
def get_random_matrix(n_lines, n_columns):
    matrix = W(n_lines, n_columns)
    for a in range(1, n_lines+1):
        for r in range(1, n_columns+1):
            matrix.t(a, r, randint(-100, 100))
    return matrix
d_1 = []
d_2 = []
for a in range(922):
    n_lines_1   = randint(5, 10)
    n_columns_1 = randint(5, 10)
    n_lines_2   = n_columns_1
    n_columns_2 = randint(5, 10)
    w_1 = get_random_matrix(n_lines_1, n_columns_1)
    w_2 = get_random_matrix(n_lines_2, n_columns_2)
    d_1.append(w_1)
    d_2.append(w_2)
d_3 = []
for i in range(len(d_2)):
    d_3.append(d_1[i]*d_2[i])

print('só para verificação da geração de valores pseudoaleatórios')
matrix = get_random_matrix(4, 6)
print(matrix)