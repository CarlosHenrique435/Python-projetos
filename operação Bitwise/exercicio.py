default_Key = 90610


def main():
    ID = None
    passcrip = None

    while True:
        try:
            name = input("Name: ").strip().rstrip()
            password = int(input("Password: "))
            if name == '':
                raise NameError
        except (EOFError, ValueError, NameError):
            print('\nPor favor digite novamente...\n')
        else:
            ID = newId(name)
            passcrip = crip(password, ID)
            break
    print(f'Usario: {ID[2:]}')
    print(f"Senha: {passcrip[2:]}")


def crip(PASS, Id):
    PASS = int(PASS ^ int(Id, 16))
    return hex(PASS)


def newId(name):
    values = []
    for c in name:
        values.append(str(ord(c)))

    values = ''.join(values)
    USERID = int(int(values) ^ default_Key)
    return hex(USERID)


if __name__ == '__main__':
    main()