class Pessoa:
    def __init__(self, nome, idade, pratoPreferido):
        self.nome = nome
        self.idade = idade
        self.pratoPreferido = pratoPreferido

    
    def mostrarComida(self):
        print(f"{self.nome} gosta d comer {self.pratoPreferido}")