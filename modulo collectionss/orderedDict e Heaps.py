def main():
    print("\nUltilizando ordereddict e Heaps com o modulo COLLECTIONS")

    from collections import OrderedDict

    print('\nPodemos criar usando compressao: ')
    dic = OrderedDict((value, str(value)) for value in range(10))
    print(dic)

    print('\nPodemos criar apartir de um objeto iteravel.')
    dic2 = OrderedDict.fromkeys('abc')
    print(dic2)

    print('\nPodemos usar a sintax normal para atribuir um valor na chava\nUsando --> dic2["a"] = 10')
    dic2["a"] = 10
    print(dic2)

    print("OrderedDict tem a função keys() e values() ou você pode percorrer com for e key ou values")
    print(dic2.keys())
    print(dic2.values())

    print('\nUm dicionario ordenado adiciona chaves de acordo com ordem de sua criação, ou seja, sempre vai adionar chaves no final')
    dic2['carlos'] = 16
    print(dic2)

    print("\nTemos a função move_to_end() --> pega o valor e move para o final.")
    print('dic2.move_to_end("b", last=False)\n'
          'last --> Se False move para o final esquerdo Se não para o final Direita')
    dic2.move_to_end('carlos', last=False)
    print(dic2)


if __name__ == '__main__':
    main()
