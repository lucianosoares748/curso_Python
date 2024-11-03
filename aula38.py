"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
qtd_linha = 5 #valor base para parar o loop
qtd_coluna = 5 #valor base para parar o loop

linha = 1 #valor inicial de linha

while linha <= qtd_linha:
    coluna = 1 #valor inicial de coluna
    
    while coluna <= qtd_coluna:
        print(f'{linha=}, {coluna=}')
        coluna += 1 #soma coluna
    
    linha += 1 #soma linha

print('Acabou')