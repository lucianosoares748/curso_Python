a = 'AAAAA'
b = 'BBBBBB'
c = 1.1

string = 'a={nome1} b={nome2} c={nome3} b={nome2}'
formato = string.format(nome1=a, nome2=b, nome3=c) #parametro noemado

print(formato) 

'''
quando uma funcao esta dentro de um objeto ela passa ser chamada de METHODO
neste exemplo acima, string(objeto), format(funcao) que passou a ser o methodo e 
o que esta dentro do methodo(), e recebeu os nomes de nome1, nome2, nome3 sao os 
parametros nomeado e quando vc nomeia o primeiro tera que nomear todos que virao apos
isso nao permite que vc nomeia um sim e outro nao
'''
