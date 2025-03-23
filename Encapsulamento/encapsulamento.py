class Conta:
    def __init__(self, saldo = 0):
        self.__saldo = saldo
    
    def deposito(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def mostrar_saldo(self):
        return self.__saldo   