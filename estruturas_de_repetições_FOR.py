texto = input('Digite uma palavra: ')
VOGAIS = 'A E I O U'


#exemplo de iteravel
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print()




#exemplo usando o built-in range

for numero in range(0, 51, 5):
   print(numero)      

