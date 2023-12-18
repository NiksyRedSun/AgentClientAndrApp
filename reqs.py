import requests
import json
import random




def get_all_active_agents():

    r = requests.request("GET", url="http://127.0.0.1:8000/agents/getallactive")

    return json.loads(r.text)



def get_all_clients():

    r = requests.request("GET", url="http://127.0.0.1:8000/agents/clients")

    return json.loads(r.text)


def get_all_events():

    r = requests.request("GET", url="http://127.0.0.1:8000/agents/events")

    return json.loads(r.text)



# print(get_all_events())