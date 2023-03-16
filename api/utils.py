
import requests
import os

auth_username = os.environ.get('USERNAME')
auth_password = os.environ.get('PASSWORD')

ABUNDA_BASE_URL = "https://www.shopabunda.com/blog/"
ABUNDA_AUTH = (auth_username, auth_password)

class AbundaError(Exception):
    pass

def send_to_abunda_blog(data, method):
    if method not in ('POST', 'PUT', 'DELETE'):
        raise ValueError(f"Invalid method '{method}'")
    
    if method == 'DELETE':
        url = ABUNDA_BASE_URL + data
        headers = {"Content-Type": "application/json"}
        response = requests.delete(url, json=data, headers=headers, auth=ABUNDA_AUTH)
    else:
        url = ABUNDA_BASE_URL + (data['article']['abunda_slug'] if method == 'PUT' else '')
        headers = {"Content-Type": "application/json"}
        response = getattr(requests, method.lower())(url, json=data, headers=headers, auth=ABUNDA_AUTH)

    response_data = response.json()

    if response.status_code == requests.codes.created or response.status_code == requests.codes.ok or response.status_code == requests.codes.no_content:
        return response_data
    else:
        error_msg = f"Abunda API error: {response.status_code} {response_data.get('error', '')}"
        raise AbundaError(error_msg)



