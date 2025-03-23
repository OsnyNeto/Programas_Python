class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print('Motor ligado')

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{k} = {v}' for k,v in self.__dict__.items()])}"

class Motocilceta(Veiculo):
    pass

class Carro(Veiculo):
   pass

class Caminhao(Veiculo):
    def __init__(self,cor,placa,numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        if self.carregado:
            print('Caminhao carregado')
        else:
            print('Caminhao vazio')

moto = Motocilceta('preta', 'ABC-1234', 2)
moto.ligar_motor()

carro = Carro('vermelho', 'XYZ-9876', 4)
carro.ligar_motor()

caminhao = Caminhao('branco', 'QWE-4567', 6,False)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)
