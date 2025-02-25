def somar(a,b):
    return a+b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação {a} + {b} = {resultado} ")

exibir_resultado(10,5,somar)

operacao = somar

print(operacao(3,20))