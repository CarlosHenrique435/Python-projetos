def recebeData():
    from sys import stdin

    print(f'Musica recebida: {stdin.readline()[:-1]}')
    date = stdin.readline()[:-1]
    print(f'data rcebida: {date}')


if __name__ == '__main__':
    recebeData()
