from random import seed
from random import choices
from random import randint
seed(4124)
m = [4, 5, 7, 7, 1, 2, 3, 3]

def w(lista):
    # forma facil, lista.sort() ta feito...
    # bubble sort...

    # -i pk a cada iteração os ultimos elementos vão ficando logo arrumados
    # ir a cada elemento e ver se é maior que o proximo, se for troca se nao for ve o dps desse

    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

w(m)
print(m)
m_1 = choices(range(1000), k=randint(500, 1000))
m_2 = choices(range(1000), k=randint(500, 1000))
m_3 = choices(range(1000), k=randint(500, 1000))
m_4 = choices(range(1000), k=randint(500, 1000))
m_5 = choices(range(1000), k=randint(500, 1000))
print('só para verificação dos valores pseudoaleatórios gerados')
print(m_5[0])
print(m_5[1])

aux = len(m_5)

print(m_5[aux-2])
print(m_5[aux-1])

# 1.1 Depois de ordenada, por ordem crescente, o elemento no índice 599, da lista m_3, é 635.
print("\n1.1")
w(m_3)
print(m_3[599] == 635)
# 1.2 Depois de ordenada, por ordem crescente, o último elemento, da lista m_2, é 997.
print("\n1.2")
w(m_2)
print(m_2[-1])
print(m_2[-1] == 997)

#1.3 Depois de ordenada, por ordem crescente, o primeiro elemento, da lista m_1, é 0.
print("\n1.3")
w(m_1)
print(m_1[0])
print(m_1[0] == 0)

# 1.4 Depois de ordenada, por ordem crescente, o elemento no índice 726, da lista m_4, é 792.
print("\n1.4")
w(m_4)
print(m_4[726])
print(m_4[726] == 792)

# 1.5 Depois de ordenada, por ordem crescente, o elemento no índice 188, da lista m_5, é 333.
print("\n1.5")
w(m_5)
print(m_5[188])
print(m_5[188] == 333)

