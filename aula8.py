nome = ('luciano')
sobrenome = ('soares')
ano_nascimento = 1997
idade = 2024 - ano_nascimento
maior_de_idade = idade >= 18
altura_em_metros = 1.67

print(f'Nome: {nome}') #f string
print(f'Sobrenome: {sobrenome}') #f string
print(f'idade: {idade}') #f string
print(f'Ano de nascimento: {ano_nascimento}') #f string

#Adicionei condicional para responder maior ou menor de idade
if idade >= 18:
    print(f'Maior de idade?: Sim voce e maior de idade')
else:
    print(f'Maior de idade?: Voce NAO e maior de idade')


print('Altura em metros:', altura_em_metros)

