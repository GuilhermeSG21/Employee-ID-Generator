import random
import sys

Nome_Completo = input('Nome completo: ')
Idade = input('Idade: ')
endereco = input('Endereço: ')
trabalha = input('Trabalha? Sim ou Não: ')

if trabalha.strip() == '' or trabalha.lower() == 'não':
    print('Desempregado.')
    sys.exit()

anos_trabalhando = input('Quantos anos trabalhando?: ')

iniciais = ''.join([nome[0].upper() for nome in Nome_Completo.split()])

numero = random.randint(100, 999)

Id = f"{iniciais}-{Idade}-{anos_trabalhando}-{numero}"

print('Id:', Id)
