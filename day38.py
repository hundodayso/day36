import key
import requests
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


response = requests.post(exercise_endpoint, headers=headers, json=params)
response.raise_for_status()
print(response.json())
