class J:

    def __init__(self, lista):
        self.n = lista

    def k(self, num):
        cont = 0
        for i in self.n:
            if i == num:
                cont += 1
        return  cont
n = [1, 2, 3, 3, 4]
j = J(n)
print(j.k(2))
print(j.k(3))
print(j.k(5))
from random import seed
from random import randint
seed(7923)
def c():
    n = []
    for y in range(981):
        n.append(randint(1, 141))
    return n
j1 = J(c())
j2 = J(c())
j3 = J(c())
j4 = J(c())
j5 = J(c())
print('só para verificação da geração de números pseudoaleatórios')
print(j1.n[0:10])