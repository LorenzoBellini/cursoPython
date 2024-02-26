'''
Iterando Strings com while
'''

nome = 'Lorenzo Bellini' #Strings são iteráveis (pode alterar ou fazer loop)

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)