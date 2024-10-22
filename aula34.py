"""
Repetições 
While (enquanto)
Executa uma ação enquanto uma condição for verdadeira
isso pode gerar um loop infinito
"""

condicao = True

while condicao:
    nome = input('Digite um nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        print('Acabou')
        break


# Se criarmos um código de loop infinito, nada que está abaixo dele sera
# alcançado para execução.

# Podemos ter while dentro de outro while