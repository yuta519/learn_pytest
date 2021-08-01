import configparser

import requests
from shodan import Shodan

api_base_url = 'https://api.shodan.io'


def return_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_key = config['Shodan']['api_key']
    return api_key

def fetch_ip(ipaddress):
    api_key = return_api_key()
    endpoint = f'{api_base_url}/shodan/host/{ipaddress}?key={api_key}'
    response = requests.get(endpoint)
    return response.json()


def fetch_ip_info(ipaddress):
    api_key = return_api_key()
    api = Shodan(api_key)
    return api.host(ipaddress)

def fetch_notifier():
    api_key = return_api_key()
    endpoint = f'{api_base_url}/notifier?key={api_key}'
    response = requests.get(endpoint)
    return response.json()

# Can't use alert api on free account
def fetch_alert(ipaddress):
    api_key = return_api_key()
    endpoint = f'{api_base_url}/shodan/alert?key={api_key}'
    data = {"name": "DNS Alert", "filters": {"ip": ipaddress}}
    response = requests.post(endpoint, data)
    return response.json()



if __name__ == '__main__':
    print(fetch_ip('8.8.8.8'))
    print(fetch_notifier())