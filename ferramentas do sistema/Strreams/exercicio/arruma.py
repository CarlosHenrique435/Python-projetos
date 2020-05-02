def Ordem():
    lista = []
    while True:
        try:
            value = input()
        except EOFError:
            break
        else:
            if len(value) >= 1:
                lista.append(int(value))
    print(sorted(lista))


if __name__ == '__main__':
    Ordem()
