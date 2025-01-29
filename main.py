import requests
import key

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

pixel_data = {
    "date": "20250129",
    "quantity": "4.03",
}

response = requests.post(url=add_pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)