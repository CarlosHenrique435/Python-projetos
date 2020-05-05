class Meta(type):
    def __new__(meta, name, bases, dct):
        print(dct)

        a = {}
        for name, value in dct.items():
            if name.startswith("__"):
                a[name] = value
            else:
                a[name.upper()] = value
        print(a)

        return type(name, bases, a)


class Classe(metaclass=Meta):
    x = 10
    y = 13

    def hello(self):
        return "Hello"


call = Classe()
print(call.X)
print(call.Y)
print(call.HELLO())
