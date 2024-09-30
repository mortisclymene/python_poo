class Pessoa:
    #Atributos
    nome = "Fulano"
    idade = 25
    altura = 1.60

    #métodos - são os comportamentos da classe
def falar(self,texto):# self é um parâmetro obrigatório do python que informa que o método pertence à própria classe que foi criada.
    print(f"Tenho algo para te falar: {texto}")

    
    # CRIANDO OBJETOS
    pessoa1 = Pessoa()

    print(pessoa1.nome, pessoa1.idade)
    pessoa1.falar("Bom dia, hoje é segunda-feira")