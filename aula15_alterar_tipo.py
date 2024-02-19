#nome = input('Qual o seu nome? ') É como um leia que SÓ FUNCIONA NO TERMINAL! Sempre salva dados em String
#print(f'O seu nome é {nome}')
#numero_1 = int(input('Digite um número: ')) Da pra fazer assim mas não é recomendado
#numero_2 = int(input('Digite outro número: ')) Caso o usuário digite algo que não é um número, o programa quebra

numero_1 = input('Digite o primeiro número: ')
numero_2 = input('Digite o segundo número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')