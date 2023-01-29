from random import seed
from random import choices
from random import randint
seed(9422)
y = [8, 9, 10, 11, 12]

def g_1(lista):
    # forma facil
    # sum(lista)/len(lista)
    sum = 0
    for i in lista:
        sum += i
    return sum/len(lista)

def g_2(lista):
    media = g_1(lista)
    sum = 0
    for i in lista:
        sum +=(i-media)**2
    return (media, sum/len(lista))

f_1 = g_1(y)
f_2 = g_2(y)
print(f_1)
print(f_2)


y_1 = choices(range(1, randint(10, 1000)), k=randint(500, 1500))
y_2 = choices(range(1, randint(10, 1000)), k=randint(500, 1500))
y_3 = choices(range(1, randint(10, 1000)), k=randint(500, 1500))
y_4 = choices(range(1, randint(10, 1000)), k=randint(500, 1500))
y_5 = choices(range(1, randint(10, 1000)), k=randint(500, 1500))


print('só para verificação dos valores pseudoaleatórios gerados')
print(y_5[0])
print(y_5[1])
print(y_5[498])
print(y_5[499])