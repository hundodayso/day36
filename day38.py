import key
import requests
import datetime
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
sheety_endpoint = "https://api.sheety.co/756305167e207d2f09c69dde414c0210/myWorkouts/workouts"





# response = requests.post(exercise_endpoint, headers=headers, json=params)
# response.raise_for_status()
# print(response.json())

sheet_params = {
    'workout':{
        'date': '11/1/1111',
        'time': '22:22:22',
        'exercise': 'walking',
        'duration': 66,
        'calories': 9999,
    }
}

add_row = requests.post(url=sheety_endpoint, json=sheet_params)
response = requests.get(url=sheety_endpoint)
response.raise_for_status()
print(response.json())



