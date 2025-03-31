from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass

    @property
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando a TV')

    def desligar(self):
        print('Desligando a TV')

    @property
    def marca(self):
        return 'Samsung'
    
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando o Ar Condicionado')

    def desligar(self):
        print('Desligando o Ar Condicionado')

    @property
    def marca(self):
        return 'LG'

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

ar = ControleArCondicionado()
ar.ligar()
ar.desligar()
print(ar.marca)
