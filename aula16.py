#if / elif ............/ else
#se / se nao se ......./ se nao

entrada = input('Voce quer "entrar" ou "sair"?')

if entrada == 'entrar':
    print('voce entrou no sistema!!')
elif entrada == 'sair':
    print('voce saiu do sistema!')
else:
    print('voce nao interagiu')

print('programa ENCERRADO')

#1 regra ==  Em um programa pode existir apenas um if e um else, se e se nao, caso seja 
#necessario

#2 regra == O elif se torna opicional e pode caso seja preciso se repetir varias vezes