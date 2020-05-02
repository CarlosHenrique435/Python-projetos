#O MODULO DBM(DATABASE) SERIA COMO O SHELVE, SERA ADICIONADO
#OS VALORES COMO UM FUNCIONAMENTO DE UM DICIONARIO. POREM OS DADOS EM STR SERÃO
#FEITOS EM BYTES.

#OBS: DBM só aceita strings como argumentos!!


"""import dbm


file = dbm.open('guarda.db', 'c')
file['carlos'] = 'carloshenriquedoliveiradasilva@gmail.com'
print(file["carlos"])
print(len(file))
print(file.keys())
file.close()"""


from urllib import request
import dbm


class error(Exception):
    def __str__(self):
        return '\033[1;31mDesculpe mas... O site digitado não exite!!\033[m'


def adiciona():
    while True:
        try:
            url = input('informe o site que a ser salvo:')

            verifica = url.find('https://')
            if verifica == -1:
                    url = f'https://{url}'
            else:
                pass
            find = request.urlopen(url)

            nome = input('Nome de busca para arquivo: ').lower()

            with dbm.open('guardaUrl.db', 'w') as file:
                file[f'{nome}'] = url

        except:
            print(error())
            print('')
        finally:
            ask = input('Deseja adicionar mais algum outro site? [S/N]')[0].upper()
            if ask == 'S':
                continue
            else:
                    chama = main()
                    break


def lista():
    name = input('Digite o nome do site salvo: ').lower()
    with dbm.open('guardaUrl.db', 'c') as file2:
        print(file2.keys())
        print(file2[f"{name}"].decode())

    ask3 = input('Deseja continuar? [S/N]').upper()[0]

    if ask3 == 'S':
        main()
    else:
        print('\n\033[1;34Até mais tarde, amigo ;)')


def main():
    while True:

        print('\033[1;33mOque deseja fazer?\033[m')
        print('\033[1;30m[ 1 ] adicionar')
        print('[ 2 ] ver minha lista')
        print('[ 3 ] fechar programa')
        try:
            askk = int(input('\n\033[1mEscolha uma opção: '))
            break
        except:
            print('\n\033[1;31mDigite o valor novamente\033[m\n')
    if askk == 1:
        adiciona()
    elif askk == 2:
        lista()
    elif askk == 3:
        print('\n\033[1;34mAté mais tarde, amigo ;)')


if __name__ == '__main__':
    main()