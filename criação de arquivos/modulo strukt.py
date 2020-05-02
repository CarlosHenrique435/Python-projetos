import struct


"""nome = b'carlos'
idade = 16

encod = struct.pack('6s I', nome, idade)

with open('codificado.txt', 'wb') as file:
    file.write(encod)

with open('codificado.txt', 'rb') as file2:
    decod = struct.unpack('6s I', file2.readline())

    print(decod)"""


class error(Exception):
    def __str__(self):
        return 'Por favor Digite seu CPF ou RG com "pontos", "/" e "-" '

while True:
    try:
        rg = input('Digite o seu RG: ')
        cpf = input('Digite seu CPF: ')

        assert(rg.count('.') == 2)
        assert(rg.count('/') == 1 or rg.count('-') == 1)

        assert(cpf.count('.') == 2)
        assert(cpf.count('-') == 1 or rg.count('/') == 1)

        break

    except:
        print(f"\n\033[1;31m{error()}")
        print('\033[1;31mTente novamente.!\033[m\n')


with open('database.txt', 'wb') as file:
    rg = rg.encode()
    cpf = cpf.encode()
    cod = struct.pack(f'{len(rg)}s {len(cpf)}s', rg, cpf)
    file.write(cod)


print('\n\033[1;34mSeus dados foram guardados!\033[1m')

per = input('\033[1;30mDeseja ver seus dados? ')[0].upper()

if per == 'S':
    with open('database.txt', 'rb') as file2:
        decod = struct.unpack(f'{len(rg)}s {len(cpf)}s', file2.readline())
        print(f'Esses são seus dados guardados em nosso banco de dados\033[1;34m', f'\033[1;30mRG: \033[1;34m{decod[0].decode()}'
                                                                                   f' \033[1;30mCPF: \033[1;34m{decod[1].decode()}')
else:
    print('Tenha um bom dia!!')
