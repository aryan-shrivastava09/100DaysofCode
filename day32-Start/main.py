import smtplib
import datetime as dt
import random
# my_email = "aryansri009@gmail.com"
# my_password = "Prioryofsion09"
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()  # TLS = Transport layer security. makes the mail encrypted
# connection.login( user= my_email, password= my_password)
# connection.sendmail(from_addr = my_email, to_addrs= "aryansri0009@yahoo.com", msg= "Subject:Hello\n\nHell fucking low")
# connection.close()

# currentdt = dt.datetime.now()
# print(currentdt)
# year = currentdt.year
# print(year)

fhand = open("./day32-Start/quotes.txt")
quotelist = fhand.readlines()
quote = random.choice(quotelist)

my_email = "aryansri009@gmail.com"
my_password = "Prioryofsion09"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user= my_email, password= my_password)
currentdt = dt.datetime.now()
day = currentdt.day
if day == 6:
    connection.sendmail(from_addr=my_email, to_addrs= "aryansri0009@yahoo.com", msg=f"Subject:Your Monday Motivation\n\n{quote}")
