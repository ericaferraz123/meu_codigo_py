from modelos.pedido import Pedido
from modelos.cliente import Cliente
from servicos.salvar import salvar_pedido
class ServicoPedido:
    def __init__(self):
        self.contador_pedidos = 1
 
    def criar_pedido(self, nome_cliente, telefone_cliente, valor_total):
        cliente = Cliente(nome_cliente, telefone_cliente)
        pedido = Pedido(self.contador_pedidos, valor_total, cliente)
        salvar_pedido(pedido)
        self.contador_pedidos += 1 