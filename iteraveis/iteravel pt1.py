#Todo iteravel tem o metodo magico __next__() e tambem tem o __iter__()


#Exemplo com for loop

"""with open("teste1.txt", 'w') as file:
    file.write('Hello\nIm Carl\nand you???')"""

#podemos percorrer um arquivo se ele tiver o iter ou next, sendo assim, ele é interavel

for c in open("teste1.txt", 'r').readlines():
    #print(c)
    pass

#podemos percorrer um arquivo que tenha o metodo next. Ex:


with open('teste1.txt', 'r') as file2:
    #print(file2.__next__())
    #print(file2.__next__())
    pass

#não podemos fazer isso com listas

lista = ['a', 'b', 'c']
print(dir(lista))
"""LISTAS NÃO PUSSUI O METODO NEXT, QUE O TORNA APENAS ITERAVEL e NÃO UM ITERADOR(Possui apenas o __ITER__())"""
#__next__ --> iterador
#iter --> iteravel


"""Mas o python nos permite transformar essa lista em um iteravel com o metodo __next__(), usando a função  
iter(args) tornando a lista um iteravel. Tambem temos a função next(i) que retornara o proximo"""


a = iter(lista)
#Aqui podemos usar o metodo next como função ou como metodo magico.
print(a.__next__())
print(a.__next__())
print(next(a))
print(dir(a))
