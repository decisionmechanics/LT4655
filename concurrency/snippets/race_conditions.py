import threading
import time

total = 0


def add(n):
    global total
    new_total = total + n
    time.sleep(1)
    total = new_total


thread1 = threading.Thread(target=add, args=(10,))
thread2 = threading.Thread(target=add, args=(20,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(total)
