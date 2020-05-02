import sys,argparse

print('argparse --> Lida com argumentos no terminal')


def fib(n):
    a, b = 0, 1
    for c in range(n):
        a,b = b, a+b
    return a


def main():
    #primeiro criamos o objeto que ira lidar com argumentos
    parse = argparse.ArgumentParser(description="Exemplo")
    #ArgumentParser --> Vai lidar com os argumentos do usuario e vai configurar

    part = 3

    if part == 1:
        part1(parse)
    elif part == 2:
        part2(parse)
    else:
        part3(parse)


def part1(parser):
    #Depois podemos colcoar argumentos
    parser.add_argument('num', help="Numero da sequencia que deseja obter", type=int)
    #arv1 --> nome do argumento
    #arv2 opcional --> Descrição do argumento
    #argv3 --> Garante que o tipo do argv sera daquele tipo

    #Depois de cinfigurar seu argumento
    #pegamos os argumentos passado no terminal
    args = parser.parse_args()

    #obtemos o resultado
    #A minha variavel arg é um objeto e para obtermos o nosso argumento bas colocar como um arumento:
    resultado = fib(args.num)
    #devolve o valor passado como num

    print(resultado)


def part2(parse):
    parse.add_argument("num", help="Valor da sequencia de fibonacci", type=int)

    parse.add_argument('-o', '--output', help='Manda a saida do programa para um arquivo', action="store_true")
    #action --> Se o argumento aparecer no terminal ele colcoa como true por isso o "store_true"
    #Você pode colocar False

    args = parse.parse_args()

    resultado = fib(args.num)

    if args.output:
        file = open('fib.txt', 'w')
        sys.stdout = file

    print(f'O resultado é {resultado}')


def part3(parse):

    parse.add_argument('num', help='valor para a sequencia', type=int)

    #Agora nos podemos especificar o arquivo em que queremos salvar para isso usamos o actio como store:
    parse.add_argument('-o', '--output', help='arquivo a ser salvo o resultado', action='store')
    #action --> pega o seguinte argumento(name file) dps do -o

    arg = parse.parse_args()

    resultado = fib(arg.num)

    if arg.output != None:
        arq = open(arg.output, 'w')
        sys.stdout = arq

    print(f'O valor {arg.num}, na sequencia é {resultado}')


if __name__ == '__main__':
    main()


"""
Podemos criar um grupu mutuante de argumentos

grupo = parse.add_mutually_group

E para adicionar argumentos no grupo usamos o add_argument()

sendo assim você só pode ter um argumento desse grupo
"""
