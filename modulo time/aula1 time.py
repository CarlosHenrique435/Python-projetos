#Biblioteca time, oque sera visto:

"""


"""

import time

print(time.asctime())

# o asctime() ira mostrar o dia, o mes a hora e o ano determinado no seu computador

#Temos o localtime() --> que retornara como uma lista em formato da classe struct_time().

print(time.localtime())
print(time.localtime()[0:2])
#Veja que você pode usar slices

#dentro do localtime() você tbm pode colocar o tempo que vc deseja ver exemplo o segundo 1
#mostrara as informações do inicio da maquina (sistema)

print(time.localtime(1))

#contando o tempo de cada linha de codigo:
print(time.process_time())

#Temos tbm o gmtime() ele retorna uma classe struct parecida com o local time porem
#a hora é contada apartir do meridiano do greenwitch, tbm podemos usar o intervalo de tempo
#apartir da epuca.

print(time.gmtime(1))
