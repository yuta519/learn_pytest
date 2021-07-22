import pytest

import fetch_shodan_api


@pytest.mark.parametrize(('ioc', 'key', 'expected'), [
    ('8.8.8.8', 'region_code', 'CA'),
    ('8.8.8.8', 'country_code', 'US'),
    ('8.8.8.8', 'city', 'Mountain View'),
    ('8.8.8.8', 'ip', 134744072),
    ('8.8.8.8', 'hostnames', ['dns.google']),
    ('8.8.8.8', 'org', 'Google LLC'),
])
def test_fetch_ip_googledns(ioc, key, expected):
    result = fetch_shodan_api.fetch_ip_info(ioc)
    assert result[key] == expected

@pytest.mark.parametrize(('ioc', 'keys'), [
    ('1.1.1.1', ['region_code','country_code','city','ip','hostnames','org'])
])
def test_fetch_ip_base(ioc, keys) -> None:
    response = fetch_shodan_api.fetch_ip_info(ioc) 
    for key in keys:
        print(key)
        assert key in response.keys()