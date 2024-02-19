'''
Introdução ao try/ Except
try -> tentar executar o código
except -> ocorreu algum erro ao executar
'''
'''
numero_str = input('Vou dobrar o número que você digitar: ')
.isdigit = Checa se foram digitados APENAS NÚMEROS, sem viírgula, espaços ou letras

if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float *2:.2f}')
else:
    print('Digite um número sem ponto ou vírgula!')
'''
numero_str = input('Vou dobrar o número que você digitar: ')

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float *2:.2f}')
except:
    print('Digite um número sem ponto ou vírgula!')