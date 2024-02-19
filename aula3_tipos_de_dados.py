"""
Python = Linguagem de Programação
Tipo de tipagem = Dinâmica (O sistema entende qual o tipo de dado está sendo usado, sem necessidade de ser especificado
Tipo de tipagem = Forte (O sistema não converte dados, só converte um tipo em outro se puder ser feito)
Str -> String -> Texto
Strings são textos que estão entre aspas
"""
print(1234) #sem necessidade de especificar o tipo de dado, o sistema já identifica

# Aspas Simples
print('Lorenzo Bellini')#Para leitura de strings, colocar texto entre Aspas Simples

# Aspas Duplas
print("Lorenzo Bellini")#Ou aspas Duplas

# Escape
print("Lorenzo \"Bellini")# Comando de escape \ faz o istema ignorar a função do próximo caractere e transforma em texto normal

# r
print(r"Lorenzo \"Bellini\"") #Caso queira que o caractere de escape seja exibido, digitar o r antes do comando

#Para evitar tudo isso pode só colocar aspas duplas dentro de aspas simples, ou vice-versa
print('Lorenzo "Bellini"')