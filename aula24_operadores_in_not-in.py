# Operadores in (entre) e not in (não entre)
# Strings são iteráveis (Pode navegar item por item)
#  0 1 2 3 4 5 6
#  L O R E N Z O
# -7-6-5-4-3-2-1
'''
nome = 'Lorenzo'
print(nome[2])
print(nome[-7])
print('L' in nome)
print('Lore' in nome)
print(10 * '--')
print('y' not in nome)
print('zero' in nome)
'''
nome = input('Digite seu nome: ')
encontrar = input('Sigite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
