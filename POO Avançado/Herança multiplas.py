#Usando Herança multipla com classes!!


class Calcula(object):
    def calc(self, exp):
        self.resultado = eval(exp)


class Out:
    def res(self):
        return f'O resultado da sua expressão é {self.resultado}'


class ite(Calcula, Out):
    pass


callAll = ite()
callAll.calc('5*5*5/5')
print(callAll.res())


#Usando o metodo super para teste
class first:
    def __init__(self):
        self.p1 = 1


class second:
    def __init__(self):
        self.p2 = 2


class Terceira(first, second):
    def __init__(self):
        super(Terceira, self).__init__()# Aqui teremos um erro, porque first e second tem o metodo construtor
                                        # iguais se um dos 2 fosse diferente não daria um erro.
        try:
            print(self.p1, self.p2)
        except Exception as E: print(E)


call = Terceira()


#Para corrigir esse erro fazemos:
class receive(first, second):
    def __init__(self):
        first.__init__(self)#Passamos como instancia a instancia dessa classe
        print(self.p1)
        second.__init__(self)
        print(self.p2)


callit = receive()
