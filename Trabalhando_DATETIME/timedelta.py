from datetime import date, datetime , timedelta,time


tipo_carro = "P" 
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_atual = data_atual + timedelta(minutes=tempo_pequeno)
    print(data_atual)
elif tipo_carro == "M":
    data_atual = data_atual + timedelta(minutes=tempo_medio)
    print(data_atual)
else:
    data_atual = data_atual + timedelta(minutes=tempo_grande)
    print(data_atual)

print(date.today() - timedelta(days=1))

resultado = datetime(2025,3,5,22,44,0) - timedelta(hours=2)
print(resultado.time())
print(datetime.now() )
print(datetime.now() + timedelta(minutes=2))
hora_alterada = datetime.now() + timedelta(hours=2)
print("Hora atual: " + datetime.now().strftime("%H:%M:%S"))
print("Hora atual alterada " + str(hora_alterada.time().strftime("%H:%M")))

