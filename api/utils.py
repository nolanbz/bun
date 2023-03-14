
import requests
import os

auth_username = os.environ.get('USERNAME')
auth_password = os.environ.get('PASSWORD')

ABUNDA_BASE_URL = "https://www.shopabunda.com/blog/"
ABUNDA_AUTH = (auth_username, auth_password)

def send_to_abunda_blog(data, method):
    """Send data to the Abunda blog API using the specified HTTP method.

    Args:
        data (dict): The data to send to the API.
        method (str): The HTTP method to use (either 'POST' or 'PUT').

    Returns:
        dict: The JSON response from the API.

    Raises:
        ValueError: If the method is not 'POST' or 'PUT'.
        AbundaError: If the API returns a non-201 status code.
    """
    if method not in ('POST', 'PUT'):
        raise ValueError(f"Invalid method '{method}'")
    
    url = ABUNDA_BASE_URL + (data['article']['abunda_slug'] if method == 'PUT' else '')
    headers = {"Content-Type": "application/json"}
    response = getattr(requests, method.lower())(url, json=data, headers=headers, auth=ABUNDA_AUTH)
    response_data = response.json()

    if response.status_code == requests.codes.created or response.status_code == requests.codes.ok:
        return response_data
    else:
        error_msg = f"Abunda API error: {response.status_code} {response_data.get('error', '')}"
        raise AbundaError(error_msg)

class AbundaError(Exception):
    pass

# def post_to_abunda_blog(data):
#     url = "https://www.shopabunda.com/blog/"

#     headers = {
#         "Content-Type": "application/json",        
#     }

#     response = requests.post(url, json=data, headers=headers, auth=(auth_username, auth_password))

#     status_code = response.status_code
#     abunda_response = response.json()

#     if status_code == 201:         
#         return abunda_response
#     else:
#         print(status_code)
#         print(abunda_response)


# def put_to_abunda_blog(data):

#     slug = data['article']['abunda_slug']

#     url = f"https://www.shopabunda.com/blog/{slug}"

#     headers = {
#         "Content-Type": "application/json",        
#     }

#     response = requests.put(url, json=data, headers=headers, auth=(auth_username, auth_password))

#     status_code = response.status_code
#     abunda_response = response.json()

#     if status_code == 201:         
#         return abunda_response
#     else:
#         print(status_code)
#         print(abunda_response)











