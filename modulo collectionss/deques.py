from collections import deque


def main():
    print('\n\033[1;34mUsando deques --> como filas\033[m')

    new = deque('ghi')# --> Você pode percorrer com for loops

    print('deque tem a função append()')
    new.append('j')# --> adiciona no final(direita)
    print('\nPossui tambem a função appendleft()')
    new.appendleft('f')# --> adicona no começo do seu deque(direita)

    print('\nTemos a função pop()')
    new.pop()# --> Remove o ultimo(direita)
    print('Temos a função popleft()')
    new.popleft()# --> Remove o ultimo(Esquerda)

    print('\nPodemos converter oque está dentro do seu deque para uma lista')
    #list(new)
    print("Podemos usar indexação e tudo oque se pode fazer com uma lista")

    print('Temos a função reverse()')
    new.reverse()# --> Sua lista fica invertidas
    print('Temos a função count()')
    print(new.count('i'))
    print('Temos a função remove()')
    new.remove('h')
    print(new)

    print('\nTemos a função exented() --> Adiona um conjuto de argumentos a direita')
    new.extend('mno')
    print(new)
    print('Temos a função extendleft() --> diciona um conjunto a esquerda')
    new.extendleft('abc')
    print(new)

    print('\n\033[1;35mE UM DOS MAIS IMPORTANTES!\033[1;30m')
    print('\nTemos a função rotate() --> Rotaciona o deque')
    new.rotate(1)
    print(new)

    print('Temos o maxlen=  que foi feito apenas para indicar o tanto q o deque aceita')
    new2 = deque('abcde', maxlen=5)
    print('Se tentado adionar com ele cheio ele retira o primeiro(esquerda) e adiona o outro no final')


if __name__ == '__main__':
    main()
