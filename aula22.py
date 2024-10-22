# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ') 

senha_permitida = '123'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida: #Usando comando or
    print('Entrou')
else:
    print('Saiu')

#Avaliacao de curto circuito
print(True or False or 0 or '')
print(False or 0 or '' or True) 

'''
Se qualquer valor for considerado verdadeiro,
a expressão inteira será avaliada naquele valor VERDADEIRO.
mesmo que eu jogue o valor true para o final, ele ira pular todos os falsos
e parar apenas la no verdadeiro como foi exemplificado na linha 24
'''