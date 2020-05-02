"""#Compressão de listas --> Forma compacta de Gerar uma lista


lista1 = [x + 10 for x in range(10)]
print(lista1)


#podemos usar com arquivos tambem.

lista2 = [linha.rstrip() for linha in open('teste1.txt')]
print(lista2)
#Isso é eficiente em memoria e em processamento(por usar apenas uma linha para isso.


print('\n\n')
#Podemos usar IFs tambem.

from random import randint

lista3 = [randint(0,100) for c in range(30) if c % 2 == 0]
print(lista3)


print('\n\n')

#podemos fazer um nested for lop

lista4 = [x + y for x in 'carlos' for y in 'anyone']
print(lista4)"""


def main():
    from random import randint

    while True:
        try:
            quantidade = int(input("Quantidade de pessoas: "))
            tentar = int(input("Quantas fezes fazer o teste: "))
        except ValueError:
            print('\n\033[1;31mTente novamente com valores inteiros\033[m\n')
        else:
            for c in range(tentar):
                listHappyB = [randint(1,365) for x in range(quantidade)]
                print(f'datas de Aniversarios {listHappyB}\n na {c+1}ª tentativa\n')

                days = [c for c in listHappyB if listHappyB.count(c) > 1]
                print(f'\033[1;30mTotal de pessoas que faz aniversário no mesmo dia:  \033[1;34m{len(days)} \033[1;30mPessoas', '\n\n')


if __name__ == '__main__':
    main()
