conta_normal = False
conta_estudante = True

saldo = 2000
saque = 2050
cheque_especial = 400

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('Atenção! Saque realizdo com cheque especial!')
    else:
        print('#Erro ao sacar. Saldo insuciente!') 
elif conta_estudante:
    if saldo >= saque:
        print('Saque realizado com sucesso!')  
    else:
        print('#Erro ao sacar. Saldo insuciente!') 
else:
    print('Não foi possivel identifcar sua conta. Entre em contato com o seu gerente.')        
