import threading
import time


def do_something():
    print(f"Running thread with ID {threading.get_ident()}")
    print(f"Running thread {threading.current_thread().name}")
    time.sleep(1)


thread = threading.Thread(target=do_something)
dave_thread = threading.Thread(name="Dave", target=do_something)

thread.start()
dave_thread.start()

thread.join()
dave_thread.join()
