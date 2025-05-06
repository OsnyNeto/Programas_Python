class Veiculo:
    def movimentar(self):
        print("Estou em movimento, poi sou veículo!")
        
    def __init__(self,fabricante,modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__numero_registro = None
        
    def getFabricanteModelo(self):
        print(f"Modelo: {self.__modelo}, Fabricante: {self.__fabricante}")
        
    def setNumeroRegistro(self, registro):
        self.__numero_registro = registro
        
    def getNumeroRegistro(self):
        return self.__numero_registro
    
    
class Carro(Veiculo):
    
    def movimentar(self):
        print("Sou um carro!")    
    
class Motocicleta(Veiculo):
    def movimentar(self):
        print("Corro muito!")
        
class Aviao(Veiculo):
    def __init__(self,fabricante,modelo,categoria):
        self.__cat = categoria
        super().__init__(fabricante,modelo)
                
    def movimentar(self):
        print("Eu voo alto!")
        
    def getCategoria(self):
        return self.__cat
    
if __name__ == '__main__':
    
    # meu_veiculo = Veiculo("GM","Onix")
    # meu_veiculo.movimentar()
    # meu_veiculo.getFabricanteModelo()
    # meu_veiculo.setNumeroRegistro("11654161-9")
    # print(f"Registro: {meu_veiculo.getNumeroRegistro()}")
    
    # meu_carro = Carro("Volvo","XC60")
    # meu_carro.movimentar()
    # meu_carro.getFabricanteModelo()
    
    # moto = Motocicleta("Triumph","Scrambler 900")
    # moto.movimentar()
    # moto.getFabricanteModelo()
    
    aviao = Aviao("Boeing","747","Comercial")
    aviao.movimentar()
    aviao.getFabricanteModelo()
    print(f"Categoria: {aviao.getCategoria()}")