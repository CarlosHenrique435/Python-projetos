

class error(Exception):
    def __str__(self):
        return 'O comando digitado acima não é aceito'


class pergunta(object):
    def __init__(self, valor1: int, valor2: int):
        self.v1 = valor1
        self.v2 = valor2

    def __repr__(self):
        return f'{self.v1 + self.v2}'


def main():
    try:
        n1 = int(input('Digite um valor:'))
        n2 = int(input('Digite mais um valor:'))
        print(pergunta(n1,n2))
    except:
        print(error())
        raise ValueError


if __name__ == '__main__':
    main()


from time import process_time

print(process_time())