class H:
    def __init__(self, w):
        self.w = w
        self.string = []

    def f(self, st):
        new_string = [st for _ in range(self.w)]
        self.string = self.string + new_string

    def j(self):
        return "".join(self.string)


teste = H(2)

teste.f("ola")
teste.f("Adeus")
print(teste.j())


class J:
    def __init__(self, n):
        self.s = n
        self.strings = []

    def j(self, string):
        self.strings.append(string)

    def r(self):
        return "".join([string * self.s for string in self.strings])

teste = J(2)

teste.j("ola")
teste.j("Adeus")
print(teste.r())

"""
class H:
    def __init__(self, n_vezes):
        self.w = n_vezes
        self.strings = ''

    def f(self, string):
        i = 0
        while i < self.w:
            self.strings += string
            i += 1

    def r(self):
        return self.strings
"""
#teste = K(2)

#teste.f("ola")
#teste.f("Adeus")
#print(teste.r())


class H:
    def __init__(self, n_vezes):
        self.w = n_vezes
        self.strings = ''

    def f(self, string):
        i = 0
        while i < self.w:
            self.strings += string
            i += 1

    def r(self):
        return self.strings


w = 3
h = H(w)
print(h.w)
content = h.r()
print('"' + content + '"')
h.f('1')
content = h.r()
print('"' + content + '"')
h.f('2')
content = h.r()
print('"' + content + '"')
h.f('xyz')
content = h.r()
print('"' + content + '"')

from random import seed
from random import choice
from random import randint

seed(1073)


def get_random_object():
    w = randint(1, 20)
    h = H(w)
    for n in range(50):
        random_string = choice('abcdefghijklmnopqrstuvwxyz')
        h.f(random_string)
    return h


t = []
for n in range(1043):
    t.append(get_random_object())

print('só para verificação da geração de números pseudoaleatórios')
print(t[1043 - 1].r()[0])
print(t[1043 - 1].r()[1])
print(t[1043 - 1].r()[2])

print('pergunta 1')
print(t[399].r()[37] =='t')

print('pergunta 2')
print(t[881].r()[383] == 'o')

print('pergunta 3')
print(t[697].r()[504] == 'b')

print('pergunta 4')
print(t[13].w)

print('pergunta 5')
print(t[435].r()[119] == 'g')




