from random import seed
from random import choices
from random import randint

alphabet = 'abcdefghijklmnopqrstuvwxyz'
class E:
    # Encrypt
    def __init__(self, plaintext, key):
        self.plaintext = plaintext
        self.key = key

    def i(self):
        encrypted = ""
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for char in self.plaintext:
            if char != ' ':
                pos = alphabet.index(char) + self.key
                if pos > 25:
                    pos = (alphabet.index(char) + self.key) - 26
                encrypted += alphabet[pos]
            else:
                encrypted += ' '
        return encrypted


class H:
    # decrypt
    def __init__(self, encryptedtext, key):
        self.encryptedtext = encryptedtext
        self.key = key

    def s(self):
        decrypted = ""
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for char in self.encryptedtext:
            if char != ' ':
                pos = alphabet.index(char) - self.key
                if pos < 0:
                    pos = (alphabet.index(char) - self.key) + 26
                decrypted += alphabet[pos]
            else:
                decrypted += ' '
        return decrypted




plaintext_string  = 'hello python world'
print(plaintext_string)
plaintext         = E(plaintext_string, 4)
ciphertext_string = plaintext.i()
print(ciphertext_string)
ciphertext        = H(ciphertext_string, 4)
decrypt_string    = ciphertext.s()
print(decrypt_string)


seed(6234)

x_1 = []
x_2 = []
for r in range(1015):
    random_string = ''.join(choices(alphabet + ' ', k=randint(400, 500)))
    shift = randint(1, 25)
    an_object = E(random_string, shift)
    x_1.append(an_object)
    random_string = ''.join(choices(alphabet + ' ', k=randint(400, 500)))
    shift = randint(1, 25)
    an_object = H(random_string, shift)
    x_2.append(an_object)
print('só para verificação da geração de números pseudoaleatórios')
print(random_string[0])
print(random_string[1])
print(random_string[2])
print(random_string[3])
print(random_string[4])