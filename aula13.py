#f strings 
#f strings serve para formatar strings
#EX ===>

nome = 'Luciano Soares'
peso = 87
altura = 1.67
imc = peso / 1.67**2

linha1 = f'{nome} tem {altura} de altura'
linha2 = f'pesa {peso}, quilos e seu IMC seria de'
linha3 = f'{imc:.2f}'

print(linha1)
print(linha2)
print(linha3)