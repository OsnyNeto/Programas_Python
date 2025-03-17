def somar(a,b):
    return a+b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação {a} + {b} = {resultado} ")

exibir_resultado(10,5,somar)

operacao = somar

print(operacao(3,20))

numeros = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0] 
print(numeros)

numeros = (0,1,2,3,4,5,)
numeros2 = [1,2,3,4,5,6]
print(type(numeros))
print(type(numeros2))
print(numeros)

numeros2[1] = 5
print(numeros2)