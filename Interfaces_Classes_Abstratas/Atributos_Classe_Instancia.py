class Estudante:
    # Variável de classe
    escola = "DIO"

    def __init__(self, nome, numero):
        # Variáveis de instância
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f"{self.nome} - {self.numero} - {self.escola}"
    
def mostrar_valores(*objetos):
    for objeto in objetos:
        print(objeto)

estudante1 = Estudante("João", 123836)
estudante2 = Estudante("Maria", 123837)
mostrar_valores(estudante1, estudante2)

Estudante.escola = "Python" # Variável de classe
estudante1.numero = 963852 # Variável de instância
mostrar_valores(estudante1, estudante2)