
def main():
    print(30 * '\033[1;34m-')
    print('\033[1;30mEm python temos 3 tipos de inputs, seriam eles:')
    print('stdin --> input')
    print('stdout --> output')
    print('stderr --> error')
    print('buffer --> Contem os dados de um input que manda para o output assim saindo um saida de dados')
    print(30 * '\033[1;34m-')

    print('Explicando melhor:')
    print('\n\033[1;30mprint("ola mundo") --> Aqui seria um input recebendos determinado dados')
    print('Ola mundo --> Seria o output a devolução do output para o usuario')

    print('Isso seria o mesmo com stdout, pois a função print tem como defaut esse objeto já definido dentro da função assim'
          ' devolvendo o output.')

    import sys

    sys.stdout.write('\033[1;35mOla mundo\033[1;30m\n')
    print('Na mensagem acima foi digitado o codigo: sys.stdout.write("Ola mundo")')

    print('\n\033[1;35mDa mesma forma temos o input que espera receber dados do usuario passa pelo buffer e manda para o output.\033[1;30m')

    print('\nQue seria a mesma coisa com o stdin, veja:')

    print('Nome: ', end='')
    name = sys.stdin.readline()[:-1]
    print(name)


if __name__ == '__main__':
    main()
