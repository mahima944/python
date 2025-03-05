import threading
import queue
import time

def producer(pro):
    for i in range(5):
        time.sleep(2)  
        pro.put(i)  
        print(f"Produced: {i}, ")

def consumer(con):
    for i in range(5):
        item = con.get()  
        print(f"Consumed: {item}")
        time.sleep(2)  
        con.task_done()  

q = queue.Queue()
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

producer_thread.start()
consumer_thread.start()

print("Producer and Consumer finished execution.")
