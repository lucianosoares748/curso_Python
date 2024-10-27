"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobrar o número que você Digitar: ')

try: # try -> tenta executar esse codigo abaixo:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except: # except -> Mas se no try ocorrer um erro "excessao" pula pro codigo abaixo:
    print('Isso não é um número')

# Se tivessemos que criar um algoritimo que fizesse o mesmo que está a cima, porém 
# utilizando IF e ELSE ficaria assim:
if numero_str.isdigit():

    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
else:
    print('Isso nao e um numero')



#  -----------------ANOTACOES
#SEMPRE que o usuario enviar algo seja atraves do input, essa dado 
#PRECISA ser tratado
#Toda variavel(objeto) tem atributos para serem usado basta digitar . 