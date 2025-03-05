import threading
import time
import psutil

def worker():
    """ Simulate CPU workload """
    for _ in range(10_000_000):
        pass

def monitor_cpu():
    """ Print CPU usage per core every second """
    while True:
        usage = psutil.cpu_percent(interval=1, percpu=True)
        print(f"CPU Usage Per Core: {usage}")

# Creating multiple worker threads
threads = [threading.Thread(target=worker) for _ in range(4)]

# Start CPU monitoring thread
monitor_thread = threading.Thread(target=monitor_cpu, daemon=True)
monitor_thread.start()

# Start worker threads
for t in threads:
    t.start()

# Wait for threads to finish
for t in threads:
    t.join()

print("All threads finished.")
