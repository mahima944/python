import threading
import time

class Ticket_booking:
    def __init__(self, total_tickets):
        self.total_tickets= total_tickets
        self.lock= threading.Lock()
        
    def Booking_tickets(self, name, requested_tickets):
        with self.lock:
            print(f"{name} is trying to book {requested_tickets} tickets ")
            time.sleep(2)
            
            if self.total_tickets>=requested_tickets:
                self.total_tickets-=requested_tickets
                print(f"{name} your booking is successful")
            else:
                print(f"{name} your booking is failed. Avaliable tickets {self.total_tickets}")
                
tickets= Ticket_booking(total_tickets=3)

user1= threading.Thread(target=tickets.Booking_tickets, args= ("alice", 2))
user2=threading.Thread(target= tickets.Booking_tickets, args= ("Bob",3))
user1.start()
user2.start()

user1.join()
user2.join()

print(f"the booking is now closed")

                
                
        