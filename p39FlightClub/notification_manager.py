import smtplib 
my_email = "aryansri009@gmail.com"
my_password = "Prioryofsion09" 
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self,msg):
        self.message = msg
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user= my_email, password= my_password)
        connection.sendmail(from_addr= my_email, to_addrs = "aryan.shrivastava9@gmail.com", msg= f"Subject:Low Price Alert!\n\n{self.message}")
