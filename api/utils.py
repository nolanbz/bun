
import requests
import os

auth_username = os.environ.get('USERNAME')
auth_password = os.environ.get('PASSWORD')

def post_to_abunda_blog(data):
    url = "https://www.shopabunda.com/blog/"

    headers = {
        "Content-Type": "application/json",        
    }

    response = requests.post(url, json=data, headers=headers, auth=(auth_username, auth_password))

    status_code = response.status_code
    abunda_response = response.json()

    if status_code == 201:         
        return abunda_response

    print(status_code)
    print(abunda_response)


def put_to_abunda_blog(data):

    slug = data['article']['abunda_slug']

    url = f"https://www.shopabunda.com/blog/{slug}"

    headers = {
        "Content-Type": "application/json",        
    }

    response = requests.put(url, json=data, headers=headers, auth=(auth_username, auth_password))

    status_code = response.status_code
    abunda_response = response.json()

    if status_code == 201:         
        return abunda_response

    print(status_code)
    print(abunda_response)




