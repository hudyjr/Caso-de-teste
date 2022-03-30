class Passageiro:
    def __init__(self, nome, num_passageiros=0):
        self.nome = nome
        self.num_passageiros = num_passageiros

    def incluir_passageiro(self):
        self.num_passageiros += 1

    def saida_passageiro(self):
        self.num_passageiros -= 1
