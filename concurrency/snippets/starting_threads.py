import threading
import time


def do_something(n):
    print(f"{n + 1}: Zzz...")
    time.sleep(1)


thread = threading.Thread(target=do_something, args=(0,))

print("Starting thread")
thread.start()
print("Thread running")
thread.join()
print("Finished")
