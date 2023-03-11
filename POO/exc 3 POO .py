class X:
    def __init__(self, m11, m12, m21, m22, m31, m32):
        self.matrix = ([m11,m12],[m21,m22],[m31,m32])
    def soma(self, outra_matriz):
        nova_m11 = self.matrix[0][0] + outra_matriz.matrix[0][0]
        nova_m12 = self.matrix[0][1] + outra_matriz.matrix[0][1]
        nova_m21 = self.matrix[1][0] + outra_matriz.matrix[1][0]
        nova_m22 = self.matrix[1][1] + outra_matriz.matrix[1][1]
        nova_m31 = self.matrix[2][0] + outra_matriz.matrix[2][0]
        nova_m32 = self.matrix[2][1] + outra_matriz.matrix[2][1]

        nova_matriz = X(nova_m11, nova_m12, nova_m21, nova_m22, nova_m31, nova_m32)

        return nova_matriz
    
    def __add__(self, outra_matriz):

        return self.soma(outra_matriz)
    
    def __repr__(self):
        return '[' +str(self.matrix[0][0]) + ' ' +str(self.matrix[0][1]) + ']\n'\
               + '[' +str(self.matrix[1][0]) + ' ' +str(self.matrix[1][1]) +']\n'  \
               + '[' +str(self.matrix[2][0]) + ' ' +str(self.matrix[2][1]) + ']'
    
x_1 = X(1, 2, 3, 4, 5, 6)
x_2 = X(1, 1, 2, 2, 3, 3)
x_3 = x_1 + x_2
print(x_1)
print('-----')
print(x_2)
print('-----')
print(x_3)

from random import seed
from random import randint

seed(5584)

def get_random_matrix():
    w = randint(-100, 100)
    m = randint(-100, 100)
    p = randint(-100, 100)
    n = randint(-100, 100)
    h = randint(-100, 100)
    v = randint(-100, 100)
    a_matrix = X(w, m, p, n, h, v)
    return a_matrix
c_1 = []
c_2 = []
for z in range(1088):
    c_1.append(get_random_matrix())
    c_2.append(get_random_matrix())
    
print('só para verificação da geração de números pseudoaleatórios')
print(c_2[1088-3])
print('-----')
print(c_2[1088-2])
print('-----')
print(c_2[1088-1])

c_3 = []
for i in range(len(c_1)):
    c_3.append(c_1[i] + c_2[i])

"""
print('pergunta 1')
print((c_3[241].m11) == 70)

print('pergunta 2')
print((c_3[1019].m32) == -109)

print('pergunta 3')
print((c_3[1014].m31) == -62)

print('pergunta 4')
print((c_3[893].m11) == -74)

print('pergunta 5')
print((c_3[956].m11) == -38)
"""
