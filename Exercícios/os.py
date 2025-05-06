import os

os.chdir('C:\\Teste')
print(f'Diretório atual: {os.getcwd()}')

nome_padrao = input("Qual o padrão de nomes dos arquivos a usar: ")

for contador, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        nome_arq, exten_arq = os.path.splitext(arq)
        nome_arq = nome_padrao + '_' + str(contador + 1)
        nome_novo = f'{nome_arq}{exten_arq}'
        os.rename(arq,nome_novo)
        
print(f'\n Arquivos renomeados.')