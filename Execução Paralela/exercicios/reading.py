import threading, time


def main():

    lock = threading.Lock()
    look = []
    lista = []

    for c in range(2):
        part = readthis(lock, lista)
        part.start()
        time.sleep(1)
        look.append(part)

    for check in look:
        check.join()


class readthis(threading.Thread):
    def __init__(self, lock, lista: list):
        self.lock = lock
        self.lista = lista
        threading.Thread.__init__(self)

    def run(self):
        with open('arquivo.txt', 'r')as file:
            if len(self.lista) == 0:
                read = file.readlines()[:500]
                self.lista.append(file.readlines()[:500])
                for c in read:
                    print(c)
            else:
                read = file.readlines()[500:]
                for c in read:
                    print(c)


if __name__ == '__main__':
    main()
