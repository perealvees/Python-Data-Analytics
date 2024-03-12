#Adicione uma condição para verificar se a quantidade de passos é positiva.
# Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
# Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.


'''quantidade_passos = int(input()) # quantidade de passos que o explorador deu na floresta 

if quantidade_passos <= 0: # Verifica se a quantidade de passos é positiva
    print("Nenhum passo dado na floresta.") # Imprime a mensagem caso a quantidade de passos seja zero
else:
    # Loop for para imprimir a mensagem do explorador
    for passo in range(1, quantidade_passos + 1): # Loop for para imprimir a mensagem do explorador indicando o número do passo
      if passo == 1: # Verifica se o número do passo é igual a 1
        print(f"Explorador: {passo} passo") # Imprime a mensagem do explorador indicando o número do passo
      else: # Caso contrário
        print(f"Explorador: {passo} passos") # Imprime a mensagem do explorador indicando os número dos passos (no plural)'''

item = []

item.append(input())
item.append(input())
item.append(input())

print("Lista de itens:") 
for item in item: 
    print(f'-',{item})