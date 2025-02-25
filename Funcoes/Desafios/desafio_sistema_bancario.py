menu = ("""
-------------- MENU --------------
      
      D - Depósito
        
      S - Saque
        
      E - Extrato
        
      Q - Sair
    
    Escolha uma função!
        
----------------------------------

""")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    
    opcao = input(menu).lower()
    opcoes = ["d","s","e","q"]

    if opcao == 'd':
        print("\nDepósito Selecionado!")

        
        while True:
            try:
                deposito = float(input("\nQual o valor vai ser despositado? "))
               
                if deposito>0:

                    saldo += deposito

                    extrato += f"\nValor depositado R$ {deposito:.2f}"

                    print(f"\nValor depositado R$ {deposito:.2f}")
                    print(f"\nSaldo atual R$ {saldo:.2f}")
                    break
                else:
                    print("\nOperação Falhou! \n\nValor Inválido!\n") 
                    break
            except ValueError:
                print(f"\nValor inválido.\nDigite um número válido!")

    if opcao == "s":

        if numero_saques >= LIMITE_SAQUES:
            print("\nNúmero de saques excedido!") 
        else:
            print("\nSaque Selecionado!")
            
            while True:
                try:
                    saque = float(input("\nQual o valor a ser sacado? "))

                    if saque > saldo:
                        print("\nSaldo Insuficiente!")
                        break

                    elif saque > limite:
                        print("\nO valor excede o limite permitido!")   
                        break 
                
                    elif saque <= 0:
                        print("\nValor inválido!")
                        break
                    
                    elif saque > 0 :
                        saldo -= saque

                        extrato += f"\nValor sacado R$ {saque:.2f}"

                        numero_saques += 1

                        print(f"\nValor Sacado R$ {saque:.2f}")
                        print(f"\nSaldo atual R$ {saldo:.2f}")
                        break

                except ValueError:
                    print(f"\nValor inválido.\nDigite um número válido!")

    if opcao == "e":
        
        print("\n=======Extrato=======\n")
        print("Não foram encontradas movimentações!" if not extrato else extrato)
        print(f"\nSaldo R$ {saldo:.2f}")
        print("\n=====================\n")
        

    if opcao == "q":
        break

    if opcao not in opcoes:
        print(f"\n{opcao.upper()} não é uma opção válida. Digite uma das opções!")
