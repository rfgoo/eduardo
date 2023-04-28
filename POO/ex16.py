class S:

    def __init__(self, line, col):

        self.matrix = []
        # TEM O _ PK TEM QUE TER VARIAVEL MAS COMO NAO VAMOS USAR PODE SER O _
        for _ in range(line):
            self.matrix.append([0]*col)



    def q(self, line, col, num):
        self.matrix[line-1][col-1] = num

    def g(self, line):
        return self.matrix[line-1]

    def j(self, col):
        x = []
        for i in range(len(self.matrix)):
            x.append(self.matrix[i][col-1])
        return x

    def w(self, line, col):
        return self.matrix[line-1][col-1]


    def __str__(self):
        a = ""
        for i in self.matrix:
            for j in i:
                a += str(j)
                a += ' '
            a += '\n'

        return a



n_lines   = 3
n_columns = 4

s = S(n_lines, n_columns)
print(s)

for i in range(1, n_lines+1):
    for c in range(1, n_columns+1):
        s.q(i, c, (i-1)*n_lines+(c-1))

print(s)
print(s.g(2))
print(s.j(3))
print(s.w(1, 1))
print(s.w(3, 4))
from random import seed
from random import randint
seed(2020)
def get_random_matrix(n_lines, n_columns):
    matrix = S(n_lines, n_columns)
    for i in range(1, n_lines+1):
        for c in range(1, n_columns+1):
            matrix.q(i, c, randint(-100, 100))
    return matrix
x_1 = []
x_2 = []
x_3 = []
for i in range(985):
    n_lines   = randint(10, 20)
    n_columns = randint(10, 20)
    s = get_random_matrix(n_lines, n_columns)
    x_1.append(s)
    line_number   = randint(1, n_lines)
    column_number = randint(1, n_columns)
    x_2.append(line_number)
    x_3.append(column_number)

# nao percebo o que ele pede com as listas
x_4 =[]
x_5 = []
for i in range(len(x_1)):
    x_4.append(x_1[i].g(x_2[i]))

for i in range(len(x_1)):
    x_5.append(x_1[i].j(x_3[i]))


print('só para verificação da geração de valores pseudoaleatórios')
matrix = get_random_matrix(4, 6)
print(matrix)
print(x_1[0]) # tem matrizes
print(x_2) # tem linhas
#print(x_3)
#print(x_4)
#print(x_5)

som = 0
for col in x_5:
    som += col[-1]
print(som)

