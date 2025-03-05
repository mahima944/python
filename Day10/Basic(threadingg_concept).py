import threading
import time

def single_task():
    print("Task started")
    time.sleep(2)
    print("Task completed")
    
thread = threading.Thread(target=single_task)
thread.start()
thread.join()
print("Main thread execution completed")

import threading
import time

def Art_work():
    print ("Art work started ")
    time.sleep(1)
    print("Art work completed")
thread = threading.Thread(target=Art_work)
thread.start()
print("Art work is deployed")