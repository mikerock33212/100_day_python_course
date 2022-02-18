##################### Hard Starting Project ######################
import datetime as dt
import pandas as pd
import random
import smtplib as sp
import ssl

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes.


def send_email(address, email_body):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "mikerock332@gmail.com"
    password = 'Zrz1409197'

    message = f"""Subject: Happy Birthday!\n\n
    {email_body}"""
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
        server.sendmail(sender_email, address, f'{message}')
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    else:
        server.quit()
        print('Email sent!')
# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.


date = dt.datetime.now()
month = date.month
day = date.day

# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
name_list = pd.read_csv('birthdays.csv')
dict_name = name_list.to_dict('records')

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
for name in dict_name:
    if name['month'] == month and name['day'] == day:
        receiver_name = name['name']
        receiver_email = name['email']
        picker = random.randint(1, 3)
        with open(f'letter_templates/letter_{str(picker)}.txt') as f:
            content = f.read()
            content.strip()
            content = content.replace('[NAME]', f'{receiver_name}')
            send_email(receiver_email, content)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



