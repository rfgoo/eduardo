class N:

    def __init__(self):
        self.lista = []

    def r(self, string):
        self.lista.append(string)

    def g(self):
        return '_'.join(x.upper() for x in self.lista)

    def y(self):
        return ''.join(x.capitalize() for x in self.lista)

    def i(self):
        return '_'.join(x.lower() for x in self.lista)


n = N()
print('"' + n.i() + '"')
print('"' + n.g() + '"')
print('"' + n.y() + '"')
n.r('hElLo')
print('"' + n.i() + '"')
print('"' + n.g() + '"')
print('"' + n.y() + '"')
n.r('PyThOn')
print('"' + n.i() + '"')
print('"' + n.g() + '"')
print('"' + n.y() + '"')
n.r('wOrLd')
print('"' + n.i() + '"')
print('"' + n.g() + '"')
print('"' + n.y() + '"')
from random import seed
from random import choices
from random import randint
seed(8732)
aux = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def get_random_object():
    n = N()
    for h in range(50):
        random_string = ''.join(choices(aux, k=randint(1, 20)))
        n.r(random_string)
    return n
p = []
for h in range(906):
    p.append(get_random_object())
print('só para verificação da geração de números pseudoaleatórios')
print(p[906-1].i()[0])
print(p[906-1].g()[1])
print(p[906-1].y()[2])