from shodan import Shodan

def fetch_ip_info(ipaddress):
    api = Shodan('EEQ01JvGzHCfS5Ddoui0XZMfNyKoSu1P')
    return type(api.host(ipaddress))


if __name__ == '__main__':
    print(fetch_ip_info('8.8.8.8'))