# Iterando strings com while 


nome = 'Luciano Soares' #iteraveis

tamanho_nome = len(nome) # Pega o tamanho da variavel

indice = 0 #coloca o indice inicial como 0 

novo_nome = '' # Variavel vazia para guardar o novo nome gerado pelo WHILE

while indice < len(nome): # Enquanto o indice [0] for menor que o tamanho de nome len(nome) =====> True
    letra = nome[indice] # Armazena cada letra que esta sendo capturada pelo nome[indice]
    novo_nome += f'*{letra}' # Pega a variavel nome que inicia com valor vazio e concatena com o valor da variavel letra += f'*{letra}'
    indice += 1 # Pula para o proximo indice e reinicia o loop 

print(novo_nome) # Quando o loop for encerrado aqui vai ser apresentado o resultado