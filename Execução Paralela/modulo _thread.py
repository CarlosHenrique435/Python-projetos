import _thread as thread,time


def pai(id, cont):
    for c in range(cont):
        time.sleep(1)
        #print(f"[{id}] --> {c}")


for c in range(5):
    thread.start_new_thread(pai, (c, 5))

time.sleep(5)
#print('fim')


#ULTILIZANDO TRAVAS

def pai(id,cont):
    for c in range(cont):
        lock.acquire()
        print(f"[{id}] --> {c}")
        lock.release()


lock = thread.allocate_lock()
for c in range(5):
    thread.start_new_thread(pai, (c,5))

time.sleep(6)
print('fim')
