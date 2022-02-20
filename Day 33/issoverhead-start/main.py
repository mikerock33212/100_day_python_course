import requests
from datetime import datetime
import time
import smtplib as sp
import ssl


def send_email(address):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "mikerock332@gmail.com"
    password = 'Zrz1409197'

    message = f"""Subject: Look Up Now for ISS!\n\n
    International Space Station is up your head.\n
    Look up now!"""
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


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


MY_LAT = 22.56087085 # Your latitude
MY_LONG = 113.94490240560009 # Your longitude


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    if is_night() and is_iss_overhead():
        send_email('zeze_1988zhao@hotmail.com')
        print('Email Sent, Please Heads Up!!!!!!')
    print('Job done for this time, waiting for next one.')
    time.sleep(60)
