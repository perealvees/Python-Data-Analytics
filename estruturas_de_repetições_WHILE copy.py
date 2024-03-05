opcao = -1

while opcao != 0:
    opcao=int(input("Escolha a opção desejada:\n[1] Sacar \n[2] Extrato \n[0] Encerrar atendimento\n"))
    if opcao == 1:
        print('Contando cédulas. Aguarde ...')
    elif opcao == 2:
        print('Imprimindo extrato. Aguarde ...')    
else:
    print('Obrigada por usar o banco Goiaba!')        
   