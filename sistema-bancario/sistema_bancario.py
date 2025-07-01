menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

'''

saldo = 0
extrato = ''
quantidade_saques_realizados = 0
QUANTIDADE_LIMITE_SAQUES = 3
VALOR_LIMITE_SAQUE = 500

while True:

    opcao = input(menu)

    if opcao == '1':

        valor_deposito = float(input('Digite o valor que deseja depositar: '))

        if valor_deposito <= 0:
            print('\nValor inválido, tente novamente.')
            continue

        else:
            print(f'A quantia de R$ {valor_deposito:.2f} foi depositado com sucesso.')
            saldo += valor_deposito
            extrato += f'Depósito: R$ {valor_deposito:.2f}\n'
    
    if opcao == '2':

        if quantidade_saques_realizados < QUANTIDADE_LIMITE_SAQUES:

            valor_saque = float(input('Digite o valor que deseja sacar: '))

            if valor_saque <= VALOR_LIMITE_SAQUE:

                if saldo < valor_saque:
                    print('Saldo insuficiente. Não é possível realizar o saque.')
                    continue

                else:
                    print(f'A quantia de R$ {valor_saque} foi sacado com sucesso.')
                    quantidade_saques_realizados += 1
                    saldo -= valor_saque
                    extrato += f'Saque: R$ {valor_saque:.2f}\n'
            
            else:
                print('O valor máximo por saque é de R$ 500,00')

        else:
            print('Você atingiu a quantidade limite de saques diários.')

    if opcao == '3':
        if not extrato:
            print('EXTRATO'.center(35, '='))
            print('\nNão foram realizadas movimentações\n')
            print(f'Saldo: R$ {saldo:.2f}\n')
            print(''.center(35, '='))
        else:
            print('EXTRATO'.center(35, '='))
            print(extrato)
            print(f'Saldo: R$ {saldo:.2f}')
            print(''.center(35, '='))

    if opcao == '0':
        print('\nSaindo... \nObrigado por usar nossos serviços!\n')
        break