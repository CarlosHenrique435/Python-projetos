from collections import defaultdict


def main():
    print('veremos sobre a função defaultdict do mudolu collections')
    exemplos = 2
    if exemplos == 1:
        print(countWords('bom bom bom é comer bombom'))
    else:
        print(count2("bom bom bom é comer bombom"))


def countWords(frase: str):
    contador = {}
    for palavra in frase.split(' '):
        corrente = contador.get(palavra, 0)
        contador[palavra] = corrente + 1

    return contador


def count2(texto):
    contador = defaultdict(int)
    for palavra in texto.split(' '):
        contador[palavra] += 1; #Todas vez que n estiver a chave ele chama a função int
        #e retorna criando uma nova chave com o valor 0
    return contador


if __name__ == '__main__':
    main()
