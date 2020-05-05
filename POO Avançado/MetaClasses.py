

def main():
    print('\n\033[1;30mNessa aula vemos nos aprofundar em MetaClasses')
    print('\nCriando uma classe com a função type()')
    a = MinhaClassee(idade=15, name='carlos')
    print(a)
    print(a.idade)

    print('Se uma classe um objeto de outra classe, qual classe seria essa?'
          '\nVamos ver com o metodo __class__')

    a = Umaclasse()
    print(a.__class__)#Subclasse de a é Umaclasse
    print(Umaclasse.__class__)#E vemos que a subclasse de minha classe é type logo ela é uma MetaClasse

    print('\nComo definimos nossa metaclasse:')
    print('Para definimos nossa metaclasse usamos os metodos __new__ e __init__')

    print('Crimos uma classe que herda a Metaclasse type()')
    print('Exemplo:')
    call = MinhaClasse()


def MinhaClassee(**args):
    return type("MinhaClasse", (object, ), args)


class Umaclasse: pass


class MinhaMeta(type):
    def __new__(meta, name, bases, dct):
        #name --> Nome da Classe
        #meta --> Seria a MetaClasse que foi definida como MinhaClasse.
        #bases --> As bases da classe que estou definindo(nesse caso seria apenas object)
        #dct --> Dicionario que define a classe

        print('-------------------------------')
        print('Alocando memoria para a classe', name)
        print(meta)
        print(bases)
        print(dct)
        return super(MinhaMeta, meta).__new__(meta, name, bases, dct)
        #Depois de consutar o metodo __new__ ele chama o metodo inicializador

    def __init__(self, name, bases, dct):
        print('--------------------------')
        print('Iniciando metodo construtor')
        print('inicializando minha classe: ', name)
        print(self)
        print(bases)
        print(dct)
        super(MinhaMeta, self).__init__(name, bases, dct)#Chamamos o metodo construtor de Type,
        #                                                  Para obter a classe que define minha classe


#Para definir que minha MetaClasse é MinhaMeta usamos os paretros=metaclass
class MinhaClasse(object, metaclass=MinhaMeta):

    def test(self, parem): pass

    atributo = 2


if __name__ == '__main__':
    main()
