nome = "Osny"
idade = 48
profissao = "Programador"
linguagem = "Python"

#Old Style %
print("Olá me chamo %s. Tenho %d anos, sou %s e faço o curso de %s." %(nome,idade,profissao,linguagem))

#Método format
print("Olá me chamo {}. Tenho {} anos, sou {} e faço o curso de {}.".format(nome,idade,profissao,linguagem))

print("Olá {nome} ".format(nome=nome))

#Método f strings
print(f"Olá me chamo {nome}. Tenho {idade} anos, sou {profissao} e faço o curso de {linguagem}.")

PI = 3.14159
saldo = 12362
print(f"Valor de PI: {PI}")
print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")
print(f"Valor de PI: {saldo:10.2f}")