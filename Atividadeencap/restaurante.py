class Servico:
    def __init__(self):
        self.__pedido = 0  

    def novoPedido(self):
        self.__pedido += 1  

    def cancelarPedido(self):
        if self.__pedido > 0:
            self.__pedido -= 1  
        else:
            print("Aviso!!!: Não há pedidos para cancelar.")

    def exibirPedido(self):
        return self.__pedido  