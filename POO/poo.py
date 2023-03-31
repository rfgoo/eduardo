class Carro:
    #marca = None
    #modelo = None
    #ano = None
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mudar_ano(self, valor):
        self.ano = valor
    def __str__(self):
        return f"{self.marca} {self.modelo}, de {self.ano}"

mercedes = Carro("mercedes", "Classe A", 2023)
vw = Carro("vw", "polo", 2021)
print(vw)
print(mercedes.marca)
print(mercedes.modelo)
print(mercedes.ano)
mercedes.mudar_ano(12)
print(mercedes)
