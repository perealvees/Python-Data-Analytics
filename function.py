''' funções é uma rotina, algo que você sempre tem que fazer dentro do código
então você cria uma função, e quando precisar usar ela em outra parte, só usa ela pra reaproveirar a função dela.
Ele também serve para criar parametros
'''

# nesse modo da forma manual, colocamos os "tracinhos" usando o print
'''print('-' *30)
print('ENTENDENDO FUNÇÕES')
print('-' *30)
print('BORA ANALISAR DADOS')
print('-' *30)
print('JÁ ENTENDI AGORA')
print('-' *30)'''

#usando as funções, vamos escrever os "tracinhos" uma vez apenas e memorizar ela em uma função:
'''def adicionar_tracinho():
    print('-'*30)
    
adicionar_tracinho()
print('ENTENDENDO FUNÇÕES')
adicionar_tracinho()
print('BORA ANALISAR DADOS')
adicionar_tracinho()
print('JÁ ENTENDI AGORA')
adicionar_tracinho()'''

#também podemos usar as funções

def titulo(texto):
    print('-' * 30)
    print(texto)
    print('-' * 30)

#agora cada titulo que adicionarmos, ele automaticamente vai adicionar a função "titulo"
titulo('Vamos ver agora')
titulo('Deu certo!')
titulo('Agora sim!')









