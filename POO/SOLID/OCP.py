# OCP -> Open/Closed Principle -> Principio Abierto/Cerrado, Los componentes deben poder extenderse, pero
# no modificarse.

class User:
    def __init__(self, name, email, sms, whatsapp):
        self.name = name
        self.email = email
        self.sms = sms
        self.whatsapp = whatsapp

class Notificator:
    def __init__(self, user, message):
        self.user = user
        self.message = message
    
    def notify(self):
        raise NotImplementedError

class NotificatorEmail(Notificator):
    def __init__(self, user, message):
        super().__init__(user, message)
    
    def notify(self):
        print(f"Enviando Email a {self.user.email}.")

class NotificatorSMS(Notificator):
    def __init__(self, user, message):
        super().__init__(user, message)
    
    def notify(self):
        print(f"Enviando SMS a {self.user.sms}.")

class NotificatorWhatsApp(Notificator):
    def __init__(self, user, message):
        super().__init__(user, message)
    
    def notify(self):
        print(f"Enviando WhatsApp a {self.user.whatsapp}.")

user = User("Andres", "email@gmail.com", "+11 111 111 1111", "+11 111 111 1111")
email = NotificatorEmail(user, "Email...")
email.notify()
sms = NotificatorSMS(user, "SMS...")
sms.notify()
ws = NotificatorWhatsApp(user, "WhatsApp...")
ws.notify()
