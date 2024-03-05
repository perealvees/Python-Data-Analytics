'''saldo = 3000
saque =float(input(f'Quantos reais você gostaria de sacar?'))

if saldo >= saque:
    print('Aguarde para retirar o dinheiro! ')
if saldo < saque:
    print(f'Saque maior que {saldo}R$. Você nao tem o valor suficiente.')'''

opcao = int(input('Informe a opção desejada: \n[1] SAQUE \n[2] EXTRATO \n'))

if opcao == 1:
    valor = float(input('Informe o valor que deseja sacar: '))
elif opcao == 2:
    print('Imprimindo extrato. Aguarde ... ')
else:
    print('Opção inválida! Escolha a opção [1] ou [2]')