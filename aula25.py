"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643

variavel = '%s, o preço é R$%.2f' % (nome, preco)#interpolação básica de string
print(variavel)




print('O hexadecimal de %d é %08X' % (1500, 1500))#convertendo valor para HEXADECIMAL
'''
%08X 08 vai preencher o restante com 0, o X maiusculo ira deixar tudo em maiusculo
'''
