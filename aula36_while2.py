"""
Repetições
While (Enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito: quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1 #Quem controla o ritmo do while é o contador

    if contador == 6: #Vai pular o 6
        print('Sem 6 pra você')
        continue

    if contador >=19 and contador <=27: #Pula do 19 ao 27
        print('Não vou mostrar o ', contador)
        continue

    print(contador)

    if contador == 40: #Parada/ Final do while
        break

print('Acabaste')