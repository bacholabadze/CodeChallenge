import smtplib
import requests
from datetime import datetime
import time

MY_EMAIL = ''
MY_PASSWORD = ''
GLDANI_LOCATION = (41.808743, 44.829843)

parameters = {
    "lat": GLDANI_LOCATION[0],
    "lng": GLDANI_LOCATION[1],
    "formatted": 0,
}


# ----------------------------------- ISS Location ----------------------------------------------------- #

def is_iss_overhead():
    response_iss = requests.get(url='http://api.open-notify.org/iss-now.json')
    response_iss.raise_for_status()

    data_iss = response_iss.json()
    longitude = float(data_iss['iss_position']['longitude'])
    latitude = float(data_iss['iss_position']['latitude'])

    # iss_position = (longitude, latitude)

    if GLDANI_LOCATION[0] - 5 <= longitude <= GLDANI_LOCATION[0] + 5 and \
            GLDANI_LOCATION[1] - 5 <= latitude <= GLDANI_LOCATION[1] + 5:
        return True
    else:
        print(f"{GLDANI_LOCATION[0] - 5} <= {longitude} <= {GLDANI_LOCATION[0] + 5}")
        print(f"{GLDANI_LOCATION[1] - 5} <= {latitude} <= {GLDANI_LOCATION[1] + 5}")
        print("Wait...")

# ---------------------------------- Sunrise & Sunset ------------------------------------------------------ #


def is_night():
    response = requests.get('http://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


# -------------------------------------------------------------------------------------------------------- #

while True:
    if is_night() and is_iss_overhead():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='bachukilabadze@gmail.com',
            msg="Subject:Look Up!\n\nThe ISS is above you in the sky."
        )
    time.sleep(60)
