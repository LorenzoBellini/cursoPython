nome = 'Lorenzo Bellini'
altura = 1.75
peso = 80
imc = peso / (altura * altura)

print('O indivíduo', nome, 'tem altura de:', altura, 'e peso em kg de:', peso,)
print('Portanto seu IMC é de:', imc)

#Intro a F-Strings
linha_1 = f'O indivíduo {nome} tem altura de: {altura}. E peso em kg de: {peso}'
print(linha_1)
linha_2 = f'Portanto seu IMC é de: {imc}'
print(linha_2)