import requests
from datetime import datetime

TOKEN = "pixela@gabzwrld"
USERNAME = "gabzwrld"
PIXELAURL = "https://pixe.la/v1/users"
ID = "gabzwater"
header = {
        "X-USER-TOKEN": TOKEN
    }
now = datetime.now()
today = now.strftime("%y%m%d")



def create_user():
    """This function creates a new user in the pixela site"""
    create_user = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService":  "yes",
        "notMinor": "yes"
    }

    new_user = requests.post(url=PIXELAURL, json=create_user)
    print(new_user.text)

def create_graph():
    """This function creates a graph"""
    create_graph = {
        "id": ID,
        "name": "water",
        "unit": "litres",
        "type": "float",
        "color": "sora",

    }

    response = requests.post(url=f"{PIXELAURL}/{USERNAME}/graphs", json=create_graph, headers=header)
    print(response.text)

def post_graph():
    """This functions makes a post to the graph"""

    post_update = {
        "date": f"20{today}",
        "quantity": str((1 * 50) / 100)
    }

    response = requests.post(url=f"{PIXELAURL}/{USERNAME}/graphs/{ID}", json=post_update, headers=header)
    print(response.text)

def update_graph():
    """This function updates a post on the graph"""
    # update_graph = {
    #     "unit": "litres",
    #     "type": "float"
    # }
    #
    # response1 = requests.put(url=f"{PIXELAURL}/{USERNAME}/graphs/{ID}", json=update_graph, headers=header)
    # print(f"graph update: {response1.text}")

    update_pixel = {
        "quantity": str((5 * 50) / 100)
    }
    response2 = requests.put(url=f"{PIXELAURL}/{USERNAME}/graphs/{ID}/20{today}", json=update_pixel, headers=header)
    print(f"pixel update: {response2.text}")



def delete_graph():
    """This function deletes a graph from the site"""
    response = requests.delete(url=f"{PIXELAURL}/{USERNAME}/graphs/{ID}", headers=header)
    print(response.text)

