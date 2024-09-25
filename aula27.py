"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

varialvel = 'ola mundo'
print(varialvel[5]) 
print(varialvel[4: ])#Vai mostrar do indice 4 ate o ultimo se eu n declarar nada 
print(varialvel[5:7])#vai pegar do inice 5 ate o 6 pq que o ultimo que seria 7 o python esconde
print(varialvel[:7])#se eu n declarar nada antes dos : ele pega do inicio ate o indice 7 

print(len(varialvel))#CONTA a quantidade de caracteres comecando do 1 ... e n do 0 como em indice  

#FATIAMENTO 
print(varialvel[0:8:2])
#               I:F:P 
# Aqui eu estou definido onde quero que comece o inicio, e o final F, e por ultimo
# de quando em quando sera o passo P, neste caso de 2 em 2 que ele ira mostrar
# e tambem pode ser feito com indice de forma negativo