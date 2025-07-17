# Happy birthday email sender
# From a csv file containing names, emails and birthdays,
# the program checks if today is the birthday of someone
# in the list. If that's the case, the program will choose
# one out of three birthday letters, include the person's
# name on the letter and send it to their email.
# It makes sense to set this code to run by a cloud provider
# (like pythonanywhere) every day, since the purpose is to
# check every day whether it is someone's birthday.

import smtplib
import datetime as dt
from random import choice
import pandas
import info

# sends the email given the name and the email
def send_email(name, email):
    my_email = info.email
    password = info.psw

    letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

    chosen_letter = choice(letters)
    message = ""
    with open(chosen_letter,"r") as file:
        for line in file.readlines():
            line = line.replace("[NAME]", f"{name}")
            message += line

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.ehlo()
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject: Happy Birthday!!\n\n{message}")
    connection.close()


todays_day = dt.datetime.now().day
todays_month = dt.datetime.now().month

file = pandas.read_csv("birthdays.csv")
months_list = file["month"].values
days_list = file["day"].values
names_list = file["name"].values
emails_list = file["email"].values

name = ""
email = ""

# checks if anyone's birthday and -month matches with today's date
for f in range(len(months_list)):
    if months_list[f]==todays_month and days_list[f]==todays_day:
        name = names_list[f]
        email = emails_list[f]
        send_email(name, email)







