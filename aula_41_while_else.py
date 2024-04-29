'''While/ Else'''
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    print(letra)
    i += 1
else: 
    print('O laço else foi executado')
print('Fora do While')