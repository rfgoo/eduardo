from random import seed
from random import choices
from random import randint
seed(6761)
file = open('text.txt', 'w', encoding='utf8')
#file = open('text.txt', 'w', encoding='utf8')
file.write('abcd\n')
file.write('efg\n')
file.write('hijkl\n')
file.close()

def e(name):

    file = open(name, 'r')
    linhas = file.readlines()
    file.close()
    return linhas
h = e('text.txt')
print(h)

# letra 3 da linha 2 é g
# linha -1, letra -1 pk no codigo começamos smp por 0 e nao por 1
print(h[1][2])


def write_random_file(filename):
    file = open(filename, 'w', encoding='utf8')
    n_lines = randint(500, 1000)
    for x in range(n_lines):
        n_letters = randint(500, 1000)
        random_string = ''.join(choices('abcdefghij', k=n_letters)) + '\n'
        file.write(random_string)
    file.close()
    return random_string


write_random_file('r_1.txt')
write_random_file('r_2.txt')
write_random_file('r_3.txt')
write_random_file('r_4.txt')
aux = write_random_file('r_5.txt')

print('só para verificação dos valores pseudoaleatórios gerados')
print(aux[0])
print(aux[1])
print(aux[2])
print(aux[3])

