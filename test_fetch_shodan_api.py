import requests
import pytest

import fetch_shodan_api


def test_fetch_ip_info():
    result = fetch_shodan_api.fetch_ip_info('8.8.8.8')
    assert type(result) == 'dict'

if __name__ == '__main__':
    test_fetch_ip_info()