# Descrição: Sistema bancário com as funções de depósito, saque e extrato.
# Autor: Osny Machado de Souza Neto




def menu():


    menu = ("""
    -------------- MENU --------------
        
        D - Depósito
            
        S - Saque
            
        E - Extrato
            
        NU - Novo Usuário
            
        NC - Nova Conta
            
        L - Listar Contas
            
        Q - Sair
        
        Escolha uma função!
            
    ----------------------------------

    """)
    return menu 

def depositar(saldo,deposito,extrato,/):
    while True:
                try:
                    if deposito>0:

                        saldo += deposito

                        extrato += f"\nValor depositado \tR$ {deposito:.2f}"

                        print(f"\nValor depositado R$ {deposito:.2f}")
                        print(f"\nSaldo atual R$ {saldo:.2f}")
                        break
                    else:
                        print("\nOperação Falhou! \n\nValor Inválido!\n") 
                        break
                except ValueError:
                    print(f"\nValor inválido.\nDigite um número válido!")
    return saldo,extrato

def sacar(*,saldo,saque,extrato,limite,numero_saques,LIMITE_SAQUES):

    if saque > saldo:
        print("\n@@@ Saldo Insuficiente! @@@")
        
    elif saque > limite:
        print("\n@@@ O valor excede o limite permitido! @@@")   
            
    elif numero_saques >= LIMITE_SAQUES:
        print("\n@@@ Número de saques excedido! @@@") 

    elif saque > 0 :
        saldo -= saque
        extrato += f"\nValor sacado \t\tR$ {saque:.2f}"
        numero_saques += 1

        print(f"\n$$$ Valor Sacado R$ {saque:.2f} $$$")
        print(f"\n$$$ Saldo atual R$ {saldo:.2f} $$$")
            
    return saldo,extrato,numero_saques

def exibir_extrato(saldo,/,*,extrato):
    print("\n============== Extrato ==============\n")
    print("Não foram encontradas movimentações!" if not extrato else extrato)
    print(f"\nSaldo \t\t\tR$ {saldo:.2f}")
    print("\n=====================================\n")

def novo_usuario(usuarios):
    cpf = input("\nInforme o CPF (somente números): ") 
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
        print("\n@@@ Já existe um usuário com esse CPF! @@@")
        return
    nome = input("\nInforme o nome completo: ")

    data_nascimento = input("\nInforme a data de nascimento (dd/mm/aaaa): ")

    endereco = input("\nInforme o endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome":nome,
        "data_nascimento":data_nascimento,
        "cpf":cpf,
        "endereco":endereco
    })
    print("\n### Usuário criado com sucesso! ###")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def nova_conta(agencia,numero_conta,usuarios):
    cpf = input("\nInforme o CPF do usuário: ")
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
        print(f"\nConta criada com sucesso! \nNúmero da conta: {numero_conta}")
        return{"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
    
    print("\n@@@ Usuário não encontrado! Fluxo de criação de conta encerrado! @@@\n")

def listar_contas(contas):
    if not contas:
        print("\nNenhuma conta cadastrada!")
    else:        
        for conta in contas:
            print(f"\nAgência: {conta['agencia']}")
            print(f"C/C: {conta['numero_conta']}")
            print(f"Titular: {conta['usuario']['nome']}")
            print(f"CPF: {conta['usuario']['cpf']}")
            print("="*100)
        
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while True:
        
        opcao = input(menu()).lower()

        opcoes = ["d","s","e","q","nu","nc","l"]

        if opcao == 'd':
            print("\nDepósito Selecionado!")
            deposito = float(input("\nQual o valor à ser despositado? "))
            saldo,extrato = depositar(saldo,deposito,extrato)
            
        if opcao == "s":
            print("\nSaque Selecionado!")

            saque = float(input("\nInforme o valor de saque: "))

            saldo,extrato,numero_saques = sacar(
                 saldo=saldo,
                 saque=saque,
                 extrato=extrato,
                 limite=limite,
                 numero_saques=numero_saques,
                 LIMITE_SAQUES=LIMITE_SAQUES)
            
        if opcao == "e":            
            exibir_extrato(saldo,extrato=extrato)

        if opcao == "nu":
            novo_usuario(usuarios)

        if opcao == "nc":
            numero_conta = len(contas) + 1
            print(f"\nCriando conta número {numero_conta}...")
            conta = nova_conta(AGENCIA,numero_conta,usuarios)
            
            if conta:
                contas.append(conta)

        if opcao == "l":
            listar_contas(contas)


        if opcao == "q":
            break

        if opcao not in opcoes:
            print(f"\n{opcao.upper()} não é uma opção válida. Digite uma das opções!")

main()

