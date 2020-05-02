print('\033[1;30m=' * 60,
      "\n\033[1;30mVeremos nessa aula como usar idexação em python com classes usando o metodo magico __getitem()")
print('=' * 60)


class getElements(object):
    def __getitem__(self, item):
        return item**2


receive = getElements()
for c in range(10):
    print(c, end=' ')

#slicing em python é um objeto, podemos usar ele da seguinte forma


class MinhaLista:# --> Verificação de slice
    def __getitem__(self, index):
        if isinstance(index, int):
            print('\nindexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)


a = MinhaLista()
a[1]
a[1:3]


#Temos o __setitem__() --> Para colocar um item em sua lista


class MinhaLista2:
    def __init__(self, start, step):
        self.start = start
        self.step = step
        self.modificado = {}

    def __getitem__(self, item):
        if isinstance(item, int):
            try: return self.modificado[item]
            except KeyError: return self.start + item*self.step
        else:
            if item.step == None: step = 1
            else: step = item.step
            data = []

            for c in range(item.start, item.stop, step):
                print(c)
                data.append(self[c])
            return data

    def __setitem__(self, key, value):
        self.modificado[key] = value


a = MinhaLista2(2,3)
print(a[0:10:2])
a[2] = 3
print(a.modificado)



#Temos tambem o __delitem__() --> remove elementos da sula lista/dict


class MinhaLista3:
    def __init__(self, lista):
        self.list = lista

    def __delitem__(self, key):
        del self.list[key]


a = MinhaLista3([1,2,3,4,5])
del a[2]
print(a.list)



#e por ultimos o __len__() --> apenas olha o tamanho do seu dicionario


class usansoLen():
    def __init__(self, lista):
        self.list = lista

    def __len__(self):
        return len(self.list)


a = usansoLen(['carlos', 'henrique', 'oliveira', 'silva'])
print(len(a))



#Temos o metodo __contains__() -->  faz a verificação:  valor in lista


class Olhando():
    def __init__(self, lista):
        self.list = lista

    def __contains__(self, item):
        return item in self.list


a = Olhando([1,2,3,4,5,6])
print(5 in a)
print(4 not in a)