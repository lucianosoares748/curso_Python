#f strings 
#f strings serve para formatar strings
#EX ===>

nome = input('Digite seu nome: ')
peso = input('Digite seu peso: ')
peso_float = float(peso)
altura = input('Digite sua altura: ')
altura_float = float(altura)
imc = peso_float / altura_float**2

linha1 = f'{nome} tem {altura} de altura'
linha2 = f'pesa {peso}, quilos e seu IMC seria de'
linha3 = f'{imc:.2f}'

print(linha1)
print(linha2)
print(linha3)