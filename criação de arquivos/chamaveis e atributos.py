class oi:
    def __init__(self):
        ola = 'ola'


class ola(oi):
    pass


print(ola.__bases__)
print(issubclass(ola,oi))

chama = oi()
print(isinstance(chama, oi))

print(callable(oi))


