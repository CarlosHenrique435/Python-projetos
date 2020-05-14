"""
Queues --> FIFO(fist in fist out) O primeiro objeto a entrar nela seria o primeiro a sair.
Queues já possui um thread lock
"""
import _thread as thread, queue, time

#Exemplo

consumidores = 2
produtores = 4
mensagens = 4

lock = thread.allocate_lock()
fila = queue.Queue() ## --> Criamos uma fila


def prod(id):
    for c in range(mensagens):
        time.sleep(2)
        fila.put(f'[produtor id={id} cont={c}')


def consu(id):
    while True:
        time.sleep(0.1)
        try:
            data = fila.get(block=False)
        except queue.Empty:
            pass
        else:
            with lock:
                print(f'Consumidor {id} recebeu --> {data}')


if __name__ == '__main__':
    for c in range(consumidores):
        thread.start_new_thread(consu, (c,))
    for i in range(produtores):
        thread.start_new_thread(prod, (i,))
        time.sleep(5)
    print('fim da thread')


print('\n\n\n')

import threading
terminate = []


def prod1(id):
    for c in range(mensagens):
        time.sleep(1)
        fila.put(f'[podutor id={id} cont={c}')


def consu1(id):
    while True:
        time.sleep(0.1)
        try:
            data = fila.get(block=False)
        except queue.Empty:
            pass
        else:
            with lock:
                print(f'consumidor {id} recebeu {data}')


if __name__ == '__main__':
    for c in range(consumidores):
        t1 = threading.Thread(target=prod1, args=(c, ))
        t1.daemon = True
        t1.start()

    threads = []

    for i in range(produtores):
        t2 = threading.Thread(target=prod1, args=(i, ))
        threads.append(t2)
        t2.start()

    for a in threads: a.join()
    print('fim da threading')

