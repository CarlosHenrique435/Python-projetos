"""
Diferentes assinaturas --> Representada pelo seu retorno, nome e parametros de entrada
"""


def agua(func):
    def beba(*args, **kwargs):
        lista = []

        for c in args:
            if c.isnumeric():
                c = int(c)
                c += 5
            else:
                pass
            lista.append(c)
        if len(lista) == 2:
            return func(lista[0], lista[1]) + '\nBeba mais agua então ooooo caralhoooo!!!'
        else:
            pass
    return beba


@agua
def send(name, idade):
    return f'ola Meu nome é {name} e tenho {idade}'


print(send("carlos", "16"))
