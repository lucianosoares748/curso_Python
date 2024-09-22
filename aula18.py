# if / elif      / else
# se / se não se / se não
'''
Em todo o bloco de codicoes se houver mais de um verdadero como neste exemplo que temos da condicao
2 para baixo todos verdadeiros = true, ele nao vai executar todos, vai executar apenas o primeiro
e pular o resto, saindo para fora do bloco de if, elif e else. 
'''

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('IF soznho')#no meu codigo posso ter apenas um if sozinho

print('Fora do if')