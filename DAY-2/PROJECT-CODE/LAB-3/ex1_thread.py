import threading
import time

def background_task():
    """A function that runs in a separate thread."""
    for i in range(5):
        print(f"Task running... {i}")
        time.sleep(1)

# Create and start the thread
thread = threading.Thread(target=background_task)
thread.start()

print("Main thread is free!")
