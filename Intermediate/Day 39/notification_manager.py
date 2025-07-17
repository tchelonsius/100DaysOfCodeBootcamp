import smtplib
import config

"""---------- GLOBAL VARIABLES ----------"""
MY_EMAIL = config.MY_EMAIL
EMAIL_PSW = config.EMAIL_PSW

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    # sends the email with the given message to the given email
    def send_email(self, message: str):
        my_email = MY_EMAIL
        password = EMAIL_PSW

        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.ehlo()
        connection.starttls()
        connection.login(user=my_email, password=password)

        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: Cheap flight(s) found\n\n{message}")
        connection.close()





