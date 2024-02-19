#if / elif / else
entrada = input('Você deseja entrar ou sair do programa? ')

if entrada == 'entrar'or 'Entrar' or 'ENTRAR':
    print('Você escolheu entrar, bem-vindo!')
elif entrada == 'sair'or 'Sair' or 'SAIR':
    print('Você escolheu sair, até logo!')
else:
    print('Opção inválida, até logo!')