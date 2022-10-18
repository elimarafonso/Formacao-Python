from abc import ABCMeta, abstractmethod

class Conta(metaclass = ABCMeta):
    def __init__(self, codigo):
        self.codigo = codigo
        self._saldo = 0

    def __str__(self):
        return f'Código: {self.codigo} - Saldo: {self._saldo}'

    def __eq__(self, other):
        return self.codigo == other.codigo and self._saldo == other._saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    def deposita(self, valor):
        self._saldo = valor
    @abstractmethod
    def passa_um_mes(self):
        pass

class ContaCorrente(Conta):

    def passa_um_mes(self):
        self.saldo -= 2


class ContaPoupanca(Conta):

    def passa_um_mes(self):
        self.saldo *= 1.01
        self.saldo -= 3


conta_elimar_corrente = ContaCorrente(12)
conta_elimar_poupanca = ContaPoupanca(12)

conta_elimar_poupanca.deposita(122)
'''conta_elimar_corrente.deposita(1000)
conta_elimar_poupanca.deposita(1000)

contas = [conta_elimar_corrente, conta_elimar_poupanca]

for conta in contas:
    conta.passa_um_mes() # polimorfismo
    print(f'Conta: {conta.codigo} - Saldo: {conta.saldo}')'''


valor = conta_elimar_corrente == conta_elimar_poupanca
print(f'valor {valor}')

contas = [conta_elimar_corrente, conta_elimar_poupanca]

for conta in contas:
    conta.passa_um_mes() # polimorfismo
    print(f'Conta: {conta.codigo} - Saldo: {conta.saldo}')