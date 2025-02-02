import requests
import key
from datetime import datetime

GRAPHID = "graph2"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": key.pixela_token,
    "username": key.pixela_un,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{key.pixela_un}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "walking",
    "unit": "Km",
    "type": "float",
    "color": "ichou"
}

headers = {
    "X-USER-TOKEN": key.pixela_token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

add_pixel_endpoint = f"{graph_endpoint}/{GRAPHID}"

today = datetime.now()


pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "8",
}

# response = requests.post(url=add_pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{add_pixel_endpoint}/{today.strftime("%Y%m%d")}"
updated_data = {
    "quantity": "5"
}

response = requests.delete(url=update_pixel_endpoint, headers=headers)
print(response.text)
