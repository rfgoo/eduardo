from random import seed
from random import choices
seed(2667)
i = 'aabbbbbcdddbbb'

def s(palavra, texto):
    size = len(palavra)
    cont = 0
    while len(texto)>=size:
        if len(texto)>=size:
            palavra_in = texto[:size]
            if palavra == palavra_in:
                cont += 1
                texto = texto[size:]
            else:
                texto = texto[1:]
    return cont




q_1 = s('aaa', i)
q_2 = s('bbb', i)
q_3 = s('eee', i)
print(q_1)
print(q_2)
print(q_3)
u_1 = ''.join(choices('abcdefghij', k=5000))
u_2 = ''.join(choices('abcdefghij', k=5000))
u_3 = ''.join(choices('abcdefghij', k=5000))
u_4 = ''.join(choices('abcdefghij', k=5000))
u_5 = ''.join(choices('abcdefghij', k=5000))
print('só para verificação dos valores pseudoaleatórios gerados')
print(u_5[0])
print(u_5[1])
print(u_5[998])
print(u_5[999])