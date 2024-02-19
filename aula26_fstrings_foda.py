'''
Formatação básica de strings
s - string
d - int
f - float (.<número de digitos pós virgula>f) === .2f
x ou x - Hexadecimal
(Caractere) (><^) (quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes do 0
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
'''
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:.>10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}')
print(f'{1000.371273829986:0=10,.2f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')