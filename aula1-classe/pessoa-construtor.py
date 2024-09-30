class Pessoa:
    #Criando o método construtor
    def __init__(self, nome, hobby, endereco):
        self.nome = nome
        self.hobby = hobby
        self.endereco = endereco


    def exibirDados(self):
         print(f"Olá {self.nome} seu hobby é {self.hobby} e seu endereço é {self.endereco}")


pessoa1 = Pessoa("Geraldo", "Corredor", "Rua 10 Cohab")
pessoa1.exibirDados()

pessoa2 = Pessoa("Carlos", "Artes Marciais", "Rua 10 Cohab")
pessoa2.exibirDados(pessoa2.nome)