class adicao(object):
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, outher):
        return self.valor + outher

    def __radd__(self, other):
        return self.valor + other

chama = adicao(10)
#print(chama + 8)
#print(10 + chama)


class submult(object):
    def __init__(self, valor):
        self.valor = valor

    def __sub__(self, other):
        return self.valor - other

    def __rsub__(self, other):
        return self.valor - other


sub = submult(10)
#print(sub - 5)
#print(20 - sub)


class mult(object):
    def __init__(self, valor):
        self.valor = valor

    def __mul__(self, other):
        return self.valor * other

    def __rmul__(self, other):
        return self.valor * other


multi = mult(5)
#print(multi * 5)
#print(10 * multi)


#operadores de comparação


class comparaMaior(object):
    def __init__(self, valor):
        self.valor = valor

    def __gt__(self, other):
        return self.valor > other


compara = comparaMaior(10)
#print(compara > 11)


class comparamenorIg(object):
    def __init__(self, valor):
        self.valor = valor

    def __le__(self, other):
        return self.valor <= other


menoIg = comparamenorIg(10)
#print(menoIg <= 5)


class igual(object):
    def __init__(self, valor):
        self.valor = valor

    def __eq__(self, other):
        return self.valor == other


a = igual('carlos'.upper())
print(a == 'henrique'.upper())