import configparser

import requests
from shodan import Shodan

api_base_url = 'https://api.shodan.io'

def fetch_ip(ipaddress):
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_key = config['Shodan']['api_key']
    endpoint = f'{api_base_url}/shodan/host/{ipaddress}?key={api_key}'
    response = requests.get(endpoint)
    return response.json()


def fetch_ip_info(ipaddress):
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_key = config['Shodan']['api_key']
    api = Shodan(api_key)
    return api.host(ipaddress)

if __name__ == '__main__':
    print(fetch_ip('8.8.8.8'))