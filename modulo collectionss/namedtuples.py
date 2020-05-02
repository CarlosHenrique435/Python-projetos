def main():
    print('\nUsaremos o modulo collections e veremos namedtuples')
    print("\nNamedtuples --> Substiu os dicionarios, quando seus dicionarios não precisam\n"
          "detanta flexibilidade, veremos agora:")

    from collections import namedtuple

    print('\nPodemos criar uma namedtuple da seguinte maneira:')
    Ponto = namedtuple('point', 'x y')
    #point --> Seria o nome da namedtuple
    #xy --> Seria as chaves(separada por espaços)d o seu dicionario

    print("sendo assim ponto seria um objeto.")
    ponto = Ponto(10,20) #Então criamos uma extenção para o nosso objeto Ponto
    print("Chamando nosso objeto Ponto temos:")
    print(ponto)
    print('podemos chamar X e Y como atributo para obter os valores contido neles.')
    print(ponto.x, ponto.y)
    print('\nOu usando indexação com nosso objeto.')
    print(ponto[0], ponto[1])

    print('Não podemos criar chaves com "_".')


if __name__ == '__main__':
    main()
