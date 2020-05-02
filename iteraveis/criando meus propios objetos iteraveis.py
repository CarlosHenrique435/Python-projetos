"""#criando o nosso propio objeto iteravel


class Quadrado(object):
    def __init__(self, com, fim):
        self.com = com
        self.fim = fim

    def __iter__(self):
        #Aqui criamos um objeto iterador e devolvemos a localidade apontado na memoria para o usuario
        return self

    def __next__(self):
        #Aqui temos o nosso iteravel que verifica se o começo é menor que o fim, se for menor
        #implementa um a mais no começo e retorna "self.com" a cada chamada.
        if self.com < self.fim:
            self.com += 1
            return self.com
        else:
            raise StopIteration


x = Quadrado(0,5)
for c in x:
    print(c, end=' ')

#mais pratico seria usando uma compressão de lista, porem n teria um objeto iterador, porem se você quisesse abranger
#mais a sua classe o ideal seria criar sua propia classe.


"""
#Podemos fazer 2 classes pare que podemos usar uma com um __iter__ que em vez de retorna a sua propia instancia
#retorna ela retorna um outra classe que tera o __next__ sendo assim, você podera usar ela varias vezes
"""


class Quadrado1(object):
    def __init__(self, com, fim):
        self.com = com
        self.fim = fim

    def __iter__(self):
        return Quadrado_iter(self.com, self.fim)


class Quadrado_iter(object):
    def __init__(self, com, fim):
        self.com = com
        self.fim = fim

    def __next__(self):
        if self.com < self.fim:
            self.com += 1
            return self.com
        else:
            raise StopIteration


x = Quadrado1(0,10)
print(f'\n{list(x)}')
for c in x:
    print(c)

#Assim podemos usar varias vezes ou podemos armazenar em uma lista.

"""
#Uma outra maneira de fazer isso é usando o yield no __iter__
"""


class Quadrad(object):
    def __init__(self, com, fim):
        self.com = com
        self.fim = fim

    def __iter__(self):
        for c in range(self.com+1, self.fim+1):
            yield c


print('\n')
x = Quadrad(0, 10)
for c in x:
    print(c, end=' ')

print('\n\n\n')

#Criando um range()"""

"""TERMINAR!!"""


class range(object):

    def __init__(self, ini:int=0, end:int=0, stp:int=0):
        self.ini = ini
        self.end = end
        self.step = stp

    def __iter__(self):
        if self.ini < self.end:
            return DownUP(self.ini, self.end, self.step)
        else:
            return DANW(self.ini, self.end, self.step)


class DownUP(object):
    def __init__(self, ini=0, end=0, stp=0):
        self.ini = ini
        self.end = end
        self.stp = stp

    def __next__(self):
        if self.ini < self.end:
            self.ini += self.stp
            return self.ini

        else: raise StopIteration


class DANW(object):
    def __init__(self, ini:int=0, end:int=0, stp:int=0):
        self.ini = ini
        self.end= end
        self.stp = stp

    def __next__(self):
        if self.ini > self.end:
            self.ini -= self.stp
            return self.ini
        else:
            raise StopIteration


for c in range(0,5):
    print(c)
