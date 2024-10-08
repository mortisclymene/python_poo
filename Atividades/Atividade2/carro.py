class Carro:
    #Criando o método construtor
    def __init__(self, marca, modelo, ano,precoDiaria):
        self.marca = marca
        self.modelo= modelo
        self.ano = ano
        self.precoDiaria = precoDiaria


    def exibirDados(self):
         print(f"Olá {self.nome} seu hobby é {self.hobby} e seu endereço é {self.endereco}")
