class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self._saldo = 0
    
    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if(self._saldo >= valor):
            self._saldo -= valor
            return self._saldo
        else:
            return f'Saldo insuficiente!{self._saldo}'
        
    def extrato(self):
        return f'A conta da {self.titular} possui {self._saldo} R$.'
    
class ContaCorrente(ContaBancaria):
    def __init__(self, titular):
        super().__init__(titular)
        self.__limite = 200
        
    def sacar(self, valor):
        if(self._saldo < valor):
            return f'saldo insuficiente! {self._saldo}'
        else :
            return self._valor - valor

class ContaPoupanca(ContaBancaria):
    def __init__(self, titular):
        super().__init__(titular)


conta_erica = ContaCorrente('ÉRICA')
print(conta_erica.extrato())
conta_erica.depositar(500)
print(conta_erica.extrato())
print(conta_erica.sacar(700))
# conta_erica.

# conta1 = ContaBancaria('Érica')
# print(conta1.extrato())

# conta1.depositar(100000.90)
# print(conta1.extrato())

# print(conta1.sacar(200000))
# print(conta1.sacar(10.9))

# print(conta1._saldo)
# print(conta1._saldo)
# print(f' A conta da {conta1.titular} possui {conta1.saldo} R$. ')