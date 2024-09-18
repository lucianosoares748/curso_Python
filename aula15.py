#                                              TRABALHANDO COM INPUTS
nome = input('Qual seu nome:')
print(f'Hellow, world {nome}')

numero_1 = input('Digite um numero: ')
numero_2 = input('Digite um numero: ')

print(f'{numero_1 + numero_2}') 

#return a concatenacao e nao faz a soma
#isso pq toda vez que se usa input dentro de uma variavel ele vai sempre retornar uma STR

#====================================================================================================================================

#TROCANDO O TYPE NA MESMA VARIAVEL DE INPUT(ENTRADA DE DADOS)

numero_1 = int(input('Digite um numero: '))
numero_2 = int(input('Digite um numero: '))
print(f'{numero_1 + numero_2}') #retorna o resultado CORRETO
'''
converter uma str para um numero na mesma linha que recebemos o input nao se recomenda,
por que se o usuario digitar um A em qualquer um desses lugares onde se recebe os dados de
inputs, este mesmo A n pode ser convertido para numero inteiro, o que vai quebrar o programa e o time de desenvolvedor
nao vai conseguir verificar nada   
'''
#==================================================================================================================================

#FAZENDO DA FORMA CORRETA
numero_1 = input('Digite um numero: ')#recendo dados
numero_2 = input('Digite um numero: ')

int_numero1 = int(numero_1)#fazendo a troca de type dentro desta variavel
int_numero2 = int(numero_2)

print(f'{int_numero1 + int_numero2}')

'''
Neste exemplo a gente recebe os dados na variavel numero_1 e 2, elas chegam como string mas sao numeros
e apenas na variavel int_numero1 e 2 convertemos de STR para INT, que agora sim esta correto, agora o dev
consegue verificar qual o type deste dado este assim que ele havia chegado.
'''