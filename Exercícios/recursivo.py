def fatorial(numero):
    if numero == 0 or numero ==1:
        print(numero)
        return  1
    else:
        print(numero)
        return numero * fatorial(numero-1)
    
                
num = int(input("Digite um número: "))

print (f"Fatorial de {num} é : {fatorial(num)}")

# Distribuitiva entre duas listas

numeros = [x * y for x in range(5) for y in [10,20,30]]
print(numeros)