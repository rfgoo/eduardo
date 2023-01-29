from random import seed
from random import choices
from random import randint
seed(7764)
s = [1, 1, 1, -4, 1, 2, -3]

def e(lista):
    sum = 0
    lista_sums = []
    for i in lista:
        sum +=i
        lista_sums.append(sum)
    return lista_sums

def n(lista):
    indices=[]
    for indice, i in enumerate(lista):
        if i < 0:
            indices.append(indice)
    return indices

h_1 = e(s)
h_2 = n(h_1)
print(h_1)
print(h_2)

c_1 = choices(range(-100, 95), k=randint(1000, 2000))
c_2 = choices(range(-100, 95), k=randint(1000, 2000))
c_3 = choices(range(-100, 95), k=randint(1000, 2000))
c_4 = choices(range(-100, 95), k=randint(1000, 2000))
c_5 = choices(range(-100, 95), k=randint(1000, 2000))


print('só para verificação dos valores pseudoaleatórios gerados')
print(c_5[0])
print(c_5[1])
print(c_5[998])
print(c_5[999])

# 3.1 O valor da primeira soma acumulada negativa, da lista c_2, é -67.
# somas acumuladas
first_neg = e(c_2)
print(first_neg)
#indicies das negativas
indi = n(first_neg)
print(indi)
# procurar pelo 1 indice das negativas nas somas acomuladas
print(first_neg[indi[0]])
