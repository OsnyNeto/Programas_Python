import datetime # para importar toda a biblioteca
#OPERADOR DE ASSOCIAÇÃO

curso = "curso de python"
frutas = ["laranja","pessego","maçã"]
saques = [2000,300]
print( "python" in curso)

print("pessego" not in frutas)

print( 300 in saques)

print("------")


#OPERADOR DE IDENTIDADE
var_a = 100
var_b = 200

print(var_a is var_a)

print( var_a is not var_b)


#OPERADORES DE NEGAÇÃO
contatos_emergencia = []

print(not 1000 > 1500)
print(not contatos_emergencia)
print(not "saque")
print(not "")

#Módulo
print( 10 % 3)

print("Olá Osny!")

#nome = input("Informe seu nome ")
#idade = input("Sua a idade ")

#print(f"Seu nome é {nome} e tem a idade {idade}", end="...\n")
#print(nome,idade, sep=" ... ")
#print(f"Seu nome é {nome} e tem a idade {idade}", end="...\n")

https://www.hashtagtreinamentos.com/como-trabalhar-com-tempo-no-python#:~:text=%C3%A9%20o%20datetime.-,date.,a%20data%20atual%20no%20Python.

print(5//2)
extrato = False
print("Sem extrato" if not extrato else extrato)
    
agora = datetime.datetime.now()
print(agora)
 
data = datetime.date(2021,9,25)
print(data)

print(data.ctime())

ano = data.year
mes = data.month
dia = data.day
#hora = data.hora # erro!
print(ano, mes, dia)

nova_data = data.replace(day=2)
print(nova_data)
print(data)

hoje = datetime.date.today()
print(hoje)

delta = hoje - data
print(delta)
print(type(delta))

nova_data = data + delta
print(nova_data)

hora = datetime.time

print(hora.hour)
print(hora.minute)
print(hora.second)