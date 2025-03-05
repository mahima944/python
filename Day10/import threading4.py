import threading
import time

def daemon_task():
    while True:
        print("Daemon thread is running...")
        time.sleep(2)  


daemon_thread = threading.Thread(target=daemon_task, daemon=True)

daemon_thread.start()

print("Main thread is running...")
time.sleep(5)
print("Main thread is exiting...")  
