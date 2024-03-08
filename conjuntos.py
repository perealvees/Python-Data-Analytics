''' Conjuntos(set).
Um set é uma coleção que não possui números repetidos.
Usamos para representar conjuntos matemáticos ou eliminar itens duplicáveis de um iterável.
Ou seja, ele elimina as duplicatas'''


#ex 1
'''numeros = set([1, 2, 3, 4, 1])
print(numeros)

fruta = set("abobora")
print(fruta)

carros = set(("palio", "gol","punto"))
print(carros)'''

#--------------------
'''Não tem como fatiar e achar qual é o vetor por exemplo.
Para isso você tem converter em listas.

numeros = {1, 2, 5, 2, 9, 9}
numeros = list(numeros)
print(numeros[0])
'''
#--------------------
'''Para usar com o for, a sintaxe é a mesma'''
carros = {"Gol","Corsa","Sandero"}

for carros in carros:
    print(carros)




