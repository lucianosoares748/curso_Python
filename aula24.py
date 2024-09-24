# Operadores in e not in / ESTA ENTRE E NAO ESTA ENTRE
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

nome = 'luciano'

print(nome[3])#busando pelo indice positivo
print(nome[-4])#busando pelo indice Negativo

# ------------- IN -------------------------------------
print('lu' in nome)#'lu' IN esta entra os dados da variavel nome?
print('w' in nome)#'w' IN esta entra os dados da variavel nome?

#-----------------NOT IN -------------------------------
print('lu' not in nome)#'lu' not in NAO ESTA entre os dados da variavel nome? FALSE
print('w' not in nome)#'w' not in NAO ESTA entra os dados da variavel nome? TRUE

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} nao esta em {nome}')