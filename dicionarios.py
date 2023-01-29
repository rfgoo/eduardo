from random import seed
from random import choices
from random import randint
seed(8144)
text = 'aaabccddddefabb'

def a(string):
    lista = []
    # garante que nao volta a contar uma letra ja contada pk estao ordenadas
    foo = sorted(string)
    # vai guardar a ultima já vista pk se tiver mtas seguidas assim vai ver a primeira e ignorar as outras
    bar = ""
    for i in foo:
        if i != bar:
            numero = string.count(i)
            bar = i
            lista.append((i,numero))

    return dict(lista)

y = a(text)
print(y)

aux = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

w_1 = ''.join(choices(aux, k=randint(5000, 10000)))
w_2 = ''.join(choices(aux, k=randint(5000, 10000)))
w_3 = ''.join(choices(aux, k=randint(5000, 10000)))
w_4 = ''.join(choices(aux, k=randint(5000, 10000)))
w_5 = ''.join(choices(aux, k=randint(5000, 10000)))

print('só para verificação dos valores pseudoaleatórios gerados')
print(w_5[0])
print(w_5[1])

aux = len(w_5)

print(w_5[aux-2])
print(w_5[aux-1])

# 1.1 W1 tem 170 b's
print("\n1.1")
print(w_1)
dict_w1=a(w_1)
print(dict_w1['b'], dict_w1['b'] == 170)

# 1.2 W5 tem 51 letras diferentes
# um dicionario nao permite ter chaves iguais, assim como as letras são as chaves, numero de letras diferentes são o numero de chaves
print("\n1.2")
dict_w5=a(w_5)
print(len(dict_w5.keys()), len(dict_w5.keys()) == 51)

# 1.3 A letra g é a letra que menos ocorrências tem na string w_3. (Possivelmente em conjunto com outras letras. Poderá não ser a única.)
# nao tenho a certeza se é a forma mais correta
print("\n1.3")
dict_w3=a(w_3)
val = list(dict_w3.values())
min = min(val)
print(min)
lista_min=[]
for i in dict_w3:
    if dict_w3.get(i) == min:
        print(f"A letra {i} é a letra com menos ocurrências, com {min}.")
        lista_min.append(i)
print(True if "g" in lista_min else False)

# 1.4 As letras j e M têm o mesmo número de ocorrências na string w_4.
print("\n1.4")
dict_w4 = a(w_4)
print("j, ", dict_w4.get("j"))
print("M, ", dict_w4.get("M"))
print(dict_w4.get("j") == dict_w4.get("M"))

# 1.5 A letra f é a letra que mais ocorrências tem na string w_2. (Possivelmente em conjunto com outras letras. Poderá não ser a única.)
# nao tenho a certeza se é a forma mais correta
print("\n1.5")
dict_w3=a(w_3)
val = list(dict_w3.values())
max = max(val)
print(max)
lista_max=[]
for i in dict_w3:
    if dict_w3.get(i) == max:
        print(f"A letra {i} é a letra com mais ocurrências, com {max}.")
        lista_max.append(i)
print(True if "f" in lista_max else False)

