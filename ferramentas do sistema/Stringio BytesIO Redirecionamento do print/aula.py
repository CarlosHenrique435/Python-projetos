def main():
    print('\033[1;36mImportamos o mudolo IO e vamos usar apenas o StringIO e BytesIO')

    from io import StringIO, BytesIO
    import sys, time

    print('Vamos criar um buffer --> Que armazena tudo oque foi escrito pelo usuario ou pelo programador.')

    print('\nJá criado um buffer')
    buff = StringIO()

    print('\nPodemos colocar coisas dentro dele. pegando nossa variavel buff colocando a função write.')
    buff.write('Hi Im carl\n')
    print('\nVocê pode esscrever quantas vezes quiser que ele armazenara em um buffer')

    buff.write('Pão de Batata\n')

    print('\nSaber oque está contido no seu buffer usamos a função getvalue()')
    print(buff.getvalue())

    print('\nPodemos criar um buffer com informações dentro dele.')
    buff = StringIO('Ola meu nome é:\nCarlos')
    print('buff = StringIO("Ola meu nome é:Carlos")')

    print('\nPodemos usar o readline para ler uma linha do nosso buffer.')
    print(buff.readline())

    print('\nRecriamos o nosso buffer.')
    buff = StringIO()

    print('Armazenamos nosso stdout em uma variavel temporaria.')
    temp = sys.stdout

    print('\nAgora vamos transformar o sys.stdout no nosso buffer, sendo assim o nosso print era armazenar apenas no buffer sem aparecer na tela')

    print('\nEntão colocamos nosso file do print como sendo temp para dizer que não ira para o buffer.')

    sys.stdout = buff
    print('\n Agora toda saida do print ira para o buffer', file=temp)
    print(45, 'carlos', 100111)

    print('\nEntão retornamos nosso stdouy para ser temp novamente e assim consiguimos ver os valores do nosso buffer', file=temp)

    sys.stdout = temp
    time.sleep(0.5)

    print(buff.getvalue())

    print('\n\n\033[1;34mTambem temos o BytesIO que basicamente é a mesma coisa que o StringIO porem ele guarda dados em Bytes.')

    buff = BytesIO(b'carlos\nAriane\nRafael')
    sys.stdout.write(str(buff.getvalue()))


if __name__ == '__main__':
    main()
