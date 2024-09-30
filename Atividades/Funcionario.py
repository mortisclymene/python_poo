class Funcio:
    #Criando o método construtor
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario


    def exibirDados(self):
         print(f"Olá {self.nome} seu cargo é {self.cargo} e seu salário é {self.salario}")
         
    def verificaSalario(self):
        Salario = self.salario
        if Salario <= 2000:
            print("Você tem direito a bônus")
        else:
             print("Sem direito a bônus")