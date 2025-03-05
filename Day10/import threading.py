import threading
import time

class TicketBookingSystem:
    def __init__(self, total_tickets):
        
        
        self.total_tickets = total_tickets
        self.lock = threading.Lock()

    def book_ticket(self, name, tickets_requested):
        with self.lock:
            if self.total_tickets >= tickets_requested:
                print(f"{name} is booking {tickets_requested} ticket(s)...")
                time.sleep(1)  
                self.total_tickets -= tickets_requested
                print(f"Booking successful for {name}. Remaining tickets: {self.total_tickets}")
            else:
                print(f"Sorry {name}, only {self.total_tickets} ticket(s) left. Booking failed.")

ticket_system = TicketBookingSystem(total_tickets=10)

def user_booking(name, tickets):
    ticket_system.book_ticket(name, tickets)

users = [
    ("Alice", 3),
    ("Bob", 4),
    ("Charlie", 2),
    ("David", 3),
]

threads = []
for user in users:
    t = threading.Thread(target=user_booking, args=(user[0], user[1]))
    threads.append(t)
    t.start()

# Waiting for all threads to complete
for t in threads:
    t.join()

print("All bookings processed.")
