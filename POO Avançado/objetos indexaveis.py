def main():
    print('\nUsando metodos magicos indexaveis, __getitem__, __setitem__, __len__ e __delitem__')

    print('\nAbordando Todos:')
    call = GetItem()

    try:
        print(call[2])
        print(call['ola'])
    except (IndexError, ValueError) as E: print(E)
    call[0] = 'hello'
    try:
        print(call[0])
    except IndexError as E: print(E)


class GetItem(object):
    def __init__(self):
        self.lis = []#--> Lista criada a busca do usuario

    def __getitem__(self, item):
        if isinstance(item, int):
            try: return self.lis[item]#Se a lista estiver algum argumento ele retorna na posição da index
            except IndexError: return '\033[1;30mPosição não existente.\033[m'
        else:
            raise ValueError('\033[1;30mPor favor digitar apenas valores inteiros!\033[m')

    def __setitem__(self, key, value):
        #Poderiamos usar o key caso nos colocarmos em um dicionario mas vamos usar apenas o value para a lista
        self.lis.append(value)

    def __len__(self):#Metodo Para ver o length da lista
        return len(self.lis)

    def __delitem__(self, key):#Remover algum elemento da lista
        del self.lis


if __name__ == '__main__':
    main()
