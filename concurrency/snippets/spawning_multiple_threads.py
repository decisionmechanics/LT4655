import threading
import time


def do_something(n):
    time.sleep(1)
    print(f"{n + 1}: Did something")


threads = []

for i in range(10):
    thread = threading.Thread(target=do_something, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
