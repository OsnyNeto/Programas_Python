#funções

def exibir_mensagem():
    print("Bem vindo Osny!")

exibir_mensagem()

def exibir_mesagem_2(nome):
    print(f"Bem vindo {nome}!")

exibir_mesagem_2("Luciana")

def mensagem_3(nome = "default"):
    print(f"Bem vindo {nome}!")

mensagem_3()
mensagem_3("Cauã")

#|Parametro somente por posição
def criar_carro(modelo,ano,placa,/,marca,motor,combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)
#Modo válido
criar_carro("Palio",1999,"JCV7J19",marca="Fiat",motor="1.0",combustivel="Flex")

#Modo inválido
criar_carro(modelo ="Palio",ano = 1999,placa="JCV7J19",marca="Fiat",motor="1.0",combustivel="Flex")


#|Parametro somente por Keyword
def criar_carro(*,modelo,ano,placa,marca,motor,combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)
#Modo inválido 
criar_carro("Palio",1999,"JCV7J19",marca="Fiat",motor="1.0",combustivel="Flex")

#Modo válido
criar_carro(modelo ="Palio",ano = 1999,placa="JCV7J19",marca="Fiat",motor="1.0",combustivel="Flex")