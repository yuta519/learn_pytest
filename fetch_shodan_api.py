import configparser
from shodan import Shodan

def fetch_ip_info(ipaddress):
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_key = config['Shodan']['api_key']
    print(api_key)
    api = Shodan(api_key)
    return type(api.host(ipaddress))


if __name__ == '__main__':
    print(fetch_ip_info('8.8.8.8'))