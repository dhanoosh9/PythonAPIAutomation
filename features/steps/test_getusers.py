import requests
import json
from behave import *

base_url = "https://gorest.co.in/public/v2/"


@given('I set get request endpoint')
def send_get_request(context):
    print("Request")


@when('I request to get all users')
def get_request(context):
    url = base_url + "users/"
    headers = {
        'Authorization': '9bfc82c8b2d4f5cbef036578d97b152030314a8ae3ff5ae8b8f9ecf6ba16e445'
    }
    context.response = requests.get(url=url, headers=headers)
    json_data = context.response.json()
    f_json = json.dumps(json_data, indent=4)
    print(f_json)





