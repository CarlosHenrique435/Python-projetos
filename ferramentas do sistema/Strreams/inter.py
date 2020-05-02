
def Quadrado():
    print('Terminar programa --> pressione ctrl+C')

    while True:
        try:
            value = int(input('Digite um valor inteiro: '))
        except (ValueError, KeyboardInterrupt, EOFError):
            break
        else:
            print(f'{value} ao quadrado é {value**2}')
    print('\ntchau!')


if __name__ == '__main__':
    Quadrado()
