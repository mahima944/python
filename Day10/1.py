import threading
import time

class TicketBookingSystem:
    def __init__(self, total_tickets):
        self.total_tickets = total_tickets
        self.lock = threading.Lock()  # Lock to prevent race conditions

    def book_ticket(self, name, tickets_requested):
        with self.lock:  # Ensures only one thread modifies tickets at a time
            print(f"{name} is trying to book {tickets_requested} ticket(s)...")
            time.sleep(1)  # Simulate processing time

            if self.total_tickets >= tickets_requested:
                self.total_tickets -= tickets_requested
                print(f"Booking successful for {name}. Remaining tickets: {self.total_tickets}")
            else:
                print(f"Booking failed for {name}. Only {self.total_tickets} ticket(s) left.")

# Initialize the system with 5 tickets
ticket_system = TicketBookingSystem(total_tickets=5)

# Two users trying to book tickets at the same time
user1 = threading.Thread(target=ticket_system.book_ticket, args=("Alice", 3))
user2 = threading.Thread(target=ticket_system.book_ticket, args=("Bob", 4))

# Start both threads (simultaneous booking attempts)
user1.start()
user2.start()

# Wait for both bookings to complete
user1.join()
user2.join()

print("Booking process completed.")
