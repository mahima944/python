from abc import ABC,abstractmethod
class Mail(ABC):
    @abstractmethod
    def send(self):
        pass
    


class email(Mail):
    def send(self):
        print("Email sent")
        
class sms(Mail):
    def send(self):
        print("sms sent")
        
class whatsapp(Mail):
    def send(self):
        print("whatsapp sent")
        
e=email()
e.send()
s=sms()
s.send()
w=whatsapp() 
w.send()       