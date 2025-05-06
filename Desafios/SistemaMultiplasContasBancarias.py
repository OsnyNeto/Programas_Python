''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

#TODO: Implemente a classe SistemaBancario:
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
class Sistema_Bancario:
    def __init__(self):
       self.contas = [] # Inicializa a listas de contas

    # TODO: Crie uma nova conta e adicione à lista de contas:
    def criar_conta(self,titular,saldo):
        conta = ContaBancaria(titular,saldo)
        self.contas.append(conta)

    # TODO: Liste todas as contas no formato "Titular: R$ Saldo":
    def listar_contas(self):
        saida =", ".join(f"{conta.titular}: R$ {conta.saldo}" for conta in self.contas)
        print(saida)
        for conta in self.contas:
            print(f"Titurlar: {conta.titular}, Saldo: R$ {conta.saldo}")

#TODO: Crie uma instância de SistemaBancario:
sistema = Sistema_Bancario()

# Entrada de dados do usuário
while True:
    entrada = input().strip()
    if entrada.upper() == "FIM":  
        break
    titular, saldo = entrada.split(", ")
    sistema.criar_conta(titular, int(saldo))

sistema.listar_contas()