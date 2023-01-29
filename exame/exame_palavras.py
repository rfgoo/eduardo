from random import seed
from random import choices
seed(2954)


w = 'aaabbbbbcdddbbba'

# enquanto o texto for maior que a palavra vamos buscar as primeiras x letras do texto com o tamanho da palavra e comparamos
# se for igual tiras as x letras do texto e incrementas o contador
# se for diferente tiras so a 1 letra do texto

def v(palavra, texto):
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

m_1 = v('bb', w)
m_2 = v('a', w)
m_3 = v('eeeee', w)

print(m_1)
print(m_2)
print(m_3)

t_1 = ''.join(choices('abcd', k=5000))
t_2 = ''.join(choices('abcd', k=5000))
t_3 = ''.join(choices('abcd', k=5000))
t_4 = ''.join(choices('abcd', k=5000))
t_5 = ''.join(choices('abcd', k=5000))

print('só para verificação dos valores pseudoaleatórios gerados')
print(t_5[0])
print(t_5[1])
print(t_5[998])
print(t_5[999])

# 4.1 Existem 4 ocorrências, sem sobreposição, da palavra bbacbcb no texto t_4.
print(v("bbacbcb", t_4))
print(t_4)
