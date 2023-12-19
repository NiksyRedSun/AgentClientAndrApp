import requests
import json
import random


site = "127.0.0.1:8000"

def get_all_active_agents():

    r = requests.request("GET", url=f"http://{site}/agents/getallactive")

    return json.loads(r.text)



def get_all_clients():

    r = requests.request("GET", url=f"http://{site}/agents/clients")

    return json.loads(r.text)


def get_all_events():

    r = requests.request("GET", url=f"http://{site}/agents/events")

    return json.loads(r.text)



def get_agent(id):

    r = requests.request("GET", url=f"http://{site}/agents/agent/{id}")

    return json.loads(r.text)


def get_agent_contracts(id):

    r = requests.request("GET", url=f"http://{site}/agents/agentcontracts/{id}")

    return json.loads(r.text)


def get_client(id):

    r = requests.request("GET", url=f"http://{site}/agents/client/{id}")

    return json.loads(r.text)


def get_event(id):

    r = requests.request("GET", url=f"http://{site}/agents/event/{id}")

    return json.loads(r.text)


def attempt(agent_id, client_id):

    r = requests.request("PUT", data=json.dumps({'agent': agent_id, 'client': client_id}), url=f"http://{site}/agents/attempt")

    return json.loads(r.text)


def new_agent():

    r = requests.request("PUT", url=f"http://{site}/agents/newagent")

    return json.loads(r.text)

def new_client():

    r = requests.request("PUT", url=f"http://{site}/agents/newclient")

    return json.loads(r.text)



# print(get_all_events())