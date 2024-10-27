"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variavel = 'ABC'

print(f'{variavel}')
print(f'{variavel: >10}')#Adiciona espaço a esquerda deixando espaço vazio
print(f'.{variavel: <10}.')#Adiciona espaço a direita deixando espaço vazio
print(f'{variavel: ^10}.')#Coloca ao centro deixando espaço vazio

exemplo = 1234

print(f'{exemplo:->10}')#Adiciona espaço a esquerda preenchendo com 0
print(f'{exemplo:@<10}')#Adiciona espaço a direita preenchendo com @
print(f'{exemplo:$^10}')#Coloca ao centro preenchendo com $

print(f'O hexadecimal de 1500 é {1500:08X}')#Hexadecimal com f string
