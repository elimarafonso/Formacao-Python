
class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self._saldo = 0

    def __str__(self):
        return f'Código: {self.codigo} - Saldo: {self._saldo}'

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    def deposita(self, valor):
        self._saldo = valor



conta_elimar = ContaCorrente(3242)
conta_elimar.deposita(100)