class Z:
    def __init__(self, string):
        self.string = string

    def __sub__(self, other):
        new = self.string.replace(other, '')
        return Z(new)
    def __str__(self):
        return self.string


z_1 = Z('Hello Python world!')
print(z_1)
z_2 = z_1 - 'l'
print(z_2)
z_3 = z_2 - 'o'
print(z_3)
z_4 = z_3 - 'H'
print(z_4)
z_5 = z_4 - 'x'
print(z_5)
from random import seed
from random import choices
from random import randint
seed(6048)
aux = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
v = []
for u in range(943):
    random_string = ''.join(choices(aux, k=randint(400, 500)))
    z_1 = Z(random_string)
    v.append(z_1)
print('só para verificação da geração de números pseudoaleatórios')
print(random_string[0])
print(random_string[1])
print(random_string[2])
print(random_string[3])
print(random_string[4])