import threading

#Sub escrevendo o modulo threading


class minha(threading.Thread):
    def __init__(self, id, cont, mutex):
        threading.Thread.__init__(self)
        self.id = id
        self.cont = cont
        self.lock = mutex

    def run(self):
        for c in range(self.cont):
            with self.lock:
                print(f'[{self.id}] --> {c}')


lock = threading.Lock()
veri = []

for c in range(10):
    Thread1 = minha(c,5,lock)
    Thread1.start()
    veri.append(Thread1)


for c in veri:
    c.join()
