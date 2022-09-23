import threading
import time


def do_something():
    print(f"Running thread with ID {threading.get_ident()}")
    print(f"Running thread {threading.current_thread().name}")
    time.sleep(3600)


thread = threading.Thread(target=do_something, daemon=True)

thread.start()
