# Depois de aprender usar input eu retornei a esta aula para ao inves 
# de deixar valores fixos nas variaveis, permitir que o usuario insira 
# esses valores atraves do input
nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura**2

print(nome, 'tem', altura, 'de altura')
print('pesa', peso, 'quilos e seu IMC seria de')
print(f'{imc:.2f}')#coloquei dois pontos flutuantes

# Depois de aprender condicoes eu voltei nesta aula e fiz este programa de IMC
# abaixo:
if imc >= 18.5 and imc <= 24.9:
    print('Você está com peso normal!')
elif imc >= 25 and imc <= 29.9:
    print('Você está com sobrepeso')
elif imc >= 30 and imc <= 34.9:
    print('Você está com Obesidade grau I')
elif imc >= 35 and imc <= 39.9:
    print('Obesidade grau II ou severa')
elif imc >= 40:
    print('Obesidade grau III ou mórbida')
elif imc < 16:
    print('Magreza severa')
elif imc >= 16 and imc <= 16.9:
    print('Magreza moderada')
elif imc >= 17 and imc <= 18.4:
    print('Magreza leve')
else:
    print('Você deixou campos em branco')