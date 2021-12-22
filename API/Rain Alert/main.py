import requests

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = "0b7a0f86ebc2544428b52f8fccff291b"

weather_params = {
    "lat": 41.805974,
    "lon": 44.832275,
    "appid": api_key,
    "exclude": 'current,minutely,daily'
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_ids = []

for i in range(48):
    weather_id = weather_data['hourly'][i]['weather'][0]['id']
    weather_ids.append(weather_id)

for _id, code in enumerate(weather_ids):
    if int(code) < 700:
        print(_id, ' Bring an umbrella')
