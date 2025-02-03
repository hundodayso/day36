import key
import requests
from datetime import datetime
#https://trackapi.nutritionix.com/docs/#/

GENDER = "male"
WEIGHT_KG = "200"
HEIGHT_CM = "185"
AGE = "66"


headers = {
    "x-app-id": key.nut_app_id,
    "x-app-key": key.nut_app_key
}

exercise_text = input("Which exercise did you do?")
params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = key.sheety_endpoint
sheety_header = {
    "Authorization": key.sheety_token
}


date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

response = requests.post(exercise_endpoint, headers=headers, json=params)
response.raise_for_status()
print(response.json())
data = response.json()

for exercise in data['exercises']:
    sheet_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise['name'],
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }

    add_row = requests.post(url=sheety_endpoint, json=sheet_params, headers=sheety_header)
    #response = requests.get(url=sheety_endpoint, headers=sheety_header)
    #response.raise_for_status()
    #print(response.json())



