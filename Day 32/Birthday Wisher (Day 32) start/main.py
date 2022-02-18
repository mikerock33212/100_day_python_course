# import smtplib as sp
#
# my_email = 'mikerock332@gmail.com'
# password = 'Zrz1409197'
#
# with sp.SMTP('smtp.gmail.com', 587) as connection:
#     connection.ehlo()
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs='r.zhao@stompy.io', msg=f'Subject:Today's Motivational quotes!\n\n'
#                                                                              '{}.')
#     print('Email sent!')
#
import smtplib as sp
import ssl
import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday() + 1

date_of_birth = dt.datetime(year=1988, month=4, day=12, hour=10)

with open('quotes.txt', 'r') as f:
    new_file = f.readlines()
    results = [line.strip() for line in new_file]

mes = random.choice(results)

smtp_server = "smtp.gmail.com"
port = 587
sender_email = "mikerock332@gmail.com"
password = 'Zrz1409197'

message = f"""\
Subject: Today's motivational quotes

{mes}"""
# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = sp.SMTP(smtp_server, port)
    server.ehlo()  # Can be omitted
    server.starttls(context=context)  # Secure the connection
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
    server.sendmail(sender_email, 'r.zhao@stompy.io', f'{message}')
except Exception as e:
    # Print any error messages to stdout
    print(e)
else:
    server.quit()
    print('Email sent!')
