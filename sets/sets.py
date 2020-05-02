print('sets é um objeto pre definido em python assim como list, dict, range etc')


def main():
    print('Set não possui elementos repetidos')
    print('Exemplo')
    s = set('mississippi')
    print(s)

    print('\nPodemos até usar set comprehension:\n')
    print({x for x in range(11) if x%2 == 0})

    print('Podemos adicionar valores no set com a função .add()')

    s.add(1001)
    print(s)

    print('\nTemos o metodo update que adiciona um set no outro')
    s.update({0,1,2,3,4})
    print(s)

    print('\nTemos o remove que remove o valor digitado ou levanta u  erro')
    s.remove(3)
    print(s)

    print('\nTemos o discard = remove um elemento mas não levanta erro')
    s.discard(10)
    print(s)

    print('\n temos o pop() = Remove e retorna um elemento aleatorio do set')
    s.pop()
    print(s)

    print('\nTemos o clear() = que remove todos os elementos do set')
    s.clear()
    print(s)

    print('\nTemos intersection ou & --> Verifica entre duas sets e cria uma nova apenas com resultado da compração')
    a = {"Carlos", "someone"}
    b = {"Carlos"}
    print('Podemos usar o & --> ', a & b)
    print('Usando o intersection --> ', a.intersection(b))

    print('\nPodemos obter a diferença tambem usando differece ou "-" --> Verifica a diference entre 2 sets')
    a = {'Joao', 'lucas', 'henrique'}
    b = {'Joao', 'julia'}
    print('Oque tem no que não tem no B', a.difference(b), a - b)
    print("Oque tem no B que não tem no A", b - a)

    print('\nTemos a diferença simetrica symmetric_difference() --> Pega todos os diferentes entre A e B e cria um novo set')
    print(a.symmetric_difference(b), 'Usando o ^ --> ', a ^ b)

    print('\nPodemos obter a união de 2 sets usando o union ou | ')
    print(a.union(b))
    print(a | b)

    print('\nPodemos verificar se um set é sub ou super set de outra')
    s1 = {1,2,3}
    s2 = {1,2,3,4,5}
    print('s1 < s2 = ', s1.issubset(s2))
    print('s1 > s2 = ', s1 > s2)


if __name__ == '__main__':
    main()
