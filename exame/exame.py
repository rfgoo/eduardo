from random import seed
from random import choices
from random import randint

seed(6499)


def myfunc(k):
    return (k[1], k[0])

def z(lista):
    lista.sort()
    done = 0
    lis = []
    for i in lista:
        if i != done:
            lis.append((i, lista.count(i)))
            done = i


    # ordenar por mais ocurrencias como 1 criterio e como segundo o numero maior.
    #lis.sort(key=lambda k: (k[1], k[0]), reverse=True)
    lis.sort(key=myfunc, reverse=True)
    for i in lis:
        if i[1] >= i[0]:
            return i[0]
    return -1


t_1 = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5]
q_1 = z(t_1)
print(q_1)
t_2 = [1, 2, 3, 3, 3, 4, 5]
q_2 = z(t_2)
print(q_2)
t_3 = [1, 2, 3, 4, 5]
q_3 = z(t_3)
print(q_3)
t_4 = [2, 3, 4, 5]
q_4 = z(t_4)
print(q_4)

u_1 = choices(range(1, 100), k=randint(5000, 8000))
u_2 = choices(range(1, 100), k=randint(5000, 8000))
u_3 = choices(range(1, 100), k=randint(5000, 8000))
u_4 = choices(range(1, 100), k=randint(5000, 8000))
u_5 = choices(range(1, 100), k=randint(5000, 8000))

print('só para verificação dos valores pseudoaleatórios gerados')
print(u_5[0])
print(u_5[1])

aux = len(u_5)
print(u_5[aux - 2])
print(u_5[aux - 1])

# 1.1 O maior número n, que está na lista u_5, pelo menos n vezes, é o 58
print(z(u_5)== 58)

