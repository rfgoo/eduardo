class H:

    def __init__(self, e):
        self.e = e
        # self.quero = que me dão

    def a(self):
        return list(set(self.e))

e = [1, 2, 3, 2, 1, 4, 4, 3, -3, -3, -3]
print(e)
h = H(e)
print(h.a())
from random import seed
from random import randint
seed(1880)
def w():
    e = []
    for d in range(1063):
        e.append(randint(1, 1523))
    return e
e1 = w()
e2 = w()
e3 = w()
e4 = w()
e5 = w()
print('só para verificação da geração de números pseudoaleatórios')
print(e1[0:10])
h1 = H(e1)
h2 = H(e2)
h3 = H(e3)
h4 = H(e4)
h5 = H(e5)
b1 = h1.a()
b2 = h2.a()
b3 = h3.a()
b4 = h4.a()
b5 = h5.a()