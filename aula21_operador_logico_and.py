#Operadores Lógicos
# And
# and = Todas as condições precisam ser verdadeiras
# São considerados falsy (não é falso mas é considerado falso) 0, 0.0, '', False
# Também existe None, que é considerado um não valor

'''
entrada = input('[E]ntrar [S]air ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
'''
print(True and True and True)
print( True and 0 and True)