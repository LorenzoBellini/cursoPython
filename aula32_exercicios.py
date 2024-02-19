"""
Faça  um programa que peça ao usuário para digitar um número inteiro, informe se
este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que
não é um número inteiro

O exercício em questão:
numero = input('Digite um número: ')

try:
    numero_float = float(numero)
    par_impar = numero_float % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {numero_float} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')
"""

"""
Faça umm programa que pergunte a hora ao usuário e, baseando-se no horário descrito
exiba uma saudação apropriada. Ex:
Bom dia 0-11; Boa tarde 12-17 e Boa noite 18-23

O exercício em questão:
hora = input('Digite a hora atual no modelo de 0 a 24 horas: ')
hora_int = int(hora)
if (hora_int >= 0) and (hora_int <=11):
    print('Bom Dia!')
elif (hora_int >= 12) and (hora_int <= 17):
    print('Boa Tarde!')
elif (hora_int >= 18) and (hora_int <= 23):
    print('Boa Noite!')
else:
    print('Horário inválido')
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos, escreva "Seu nome é curto"; Se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal", maior que 6 letras escreva "Seu nome é muito grande"

O exercício em questão:
nome = input('Escreva o seu nome: ')
if ((len(nome)) <= 4):
    print('Seu nome é curto')
if ((len(nome)) >= 5) and ((len(nome)) <= 6):
    print('Seu nome é normal')
if ((len(nome)) > 6):
    print('Seu nome é muito longo')
else:
    print('Digite pelo menos uma letra')
"""