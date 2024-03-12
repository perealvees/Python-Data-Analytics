''' funções é uma rotina, algo que você sempre tem que fazer dentro do código
então você cria uma função, e quando precisar usar ela em outra parte, só usa ela pra reaproveirar a função dela.'''

''' nesse modo da forma manual, colocamos os "tracinhos" usando o print
print('-' *30)
print('ENTENDENDO FUNÇÕES')
print('-' *30)
print('BORA ANALISAR DADOS')
print('-' *30)
print('JÁ ENTENDI AGORA')
print('-' *30)'''

'''usando as funções, vamos escrever os "tracinhos" uma vez apenas e memorizar ela em uma função:
def adicionar_tracinho():
    print('-'*30)
    
adicionar_tracinho()
print('ENTENDENDO FUNÇÕES')
adicionar_tracinho()
print('BORA ANALISAR DADOS')
adicionar_tracinho()
print('JÁ ENTENDI AGORA')
adicionar_tracinho()'''

'''também podemos usar as funções passando os parametros

def titulo(texto):
    print('-' * 30)
    print(texto)
    print('-' * 30)

#agora cada titulo que adicionarmos, ele automaticamente vai adicionar a função "titulo"
titulo('Vamos ver agora')
titulo('Deu certo!')
titulo('Agora sim!')'''

'''outro exemplo:
def soma(a, b):
    print(f'A = {a} e o B = {b}')
    soma = a + b
    print(f'A soma de A + B = {soma}')


soma(a=4, b=5)
soma(5, 9)'''

''' Podemos fazer um envelopamento, assim você pode passar quantos parametros quiser e a função vai agrupar tudo dentro de um argumento só"'''

def contador(*numeros):
    tam = len(numeros)
    print(f'Recebi os valores{numeros} e são ao todo {tam} parametros.')

contador(2, 5, 7, 3, 0, 2)
contador(5, 7, 0, 6, 1, 1, 1)
contador(4, 5)
contador(1, 7, 9, 5, 7)


