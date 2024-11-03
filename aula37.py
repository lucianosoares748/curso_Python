"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""


contador = 0

while contador <= 100:
    contador += 1 #Isso é o que mantem o laço de continuação
    #devemos ficar atendo a base para não criar um loop infinito


    if contador == 27:
        print('Não vou mostar o 27.')
        continue # Pula a contagem, e reinicia o loop

    if contador >= 35 and contador <= 40:
        print('Não vou mostrar o', contador)
        continue
    
    print(contador)


    if contador == 50:  
        break

# O continue vai ser aplicado sempre para o WHILE mais próximo. 